import scrapy
from scrapy.loader import ItemLoader
from flywheel_scraper.items import DetailItem


class FlywheelSpider(scrapy.Spider):
    name = "info"

    start_urls = ["https://getflywheel.com/agency-partners-directory/"]

    def parse(self, response):
        all_links = response.css(".directory-item__card-agency a::attr(href)").extract()
        yield from response.follow_all(all_links, self.parse_each)

        next_page = response.css(".pagination .nav-previous a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_each(self, response):

        each_item = ItemLoader(item=DetailItem(), response=response)
        each_item.add_value("url", response)
        each_item.add_css("business_name", "h1.feature-title::text")
        each_item.add_css("website", "p.agency-link a::attr(href)")
        each_item.add_css("detail", ".agency__intro-content p::text")
        each_item.add_css("address", ".agency-details__list span::text")
        each_item.add_css("country", ".agency-details__list p::text")
        each_item.add_css("social", ".agency-details__social a::attr(href)")

        return each_item.load_item()
