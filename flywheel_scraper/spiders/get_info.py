import scrapy


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
        yield {
            "bussiness_name": response.css("h1.feature-title::text").get(),
            "website": response.css("p.agency-link a::attr(href)").get(),
            "detail": response.css(".agency__intro-content p::text").get(),
            "address": response.css(".agency-details__list span::text").get(),
            "country": response.css(".agency-details__list p::text").get(),
            "social": response.css(".agency-details__social a::attr(href)").getall(),
        }
