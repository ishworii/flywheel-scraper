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
        each_item.add_value("url", response.url)
        each_item.add_value(
            "business_name", response.css("h1.feature-title::text").get()
        )
        website = response.css("p.agency-link a::attr(href)").get()
        each_item.add_value("website", website)
        each_item.add_value(
            "detail", response.css(".agency__intro-content p::text").get()
        )
        each_item.add_value(
            "address", response.css(".agency-details__list span::text").get()
        )
        each_item.add_value(
            "country", response.css(".agency-details__list p::text").get()
        )
        each_item.add_value(
            "social", response.css(".agency-details__social a::attr(href)").getall()
        )
        return each_item.load_item()
