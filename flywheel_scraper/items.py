# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import scrapy


# class FlywheelScraperItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DetailItem:
    url: Optional[str] = field(default=None)
    business_name: Optional[str] = field(default=None)
    website: Optional[str] = field(default=None)
    detail: Optional[str] = field(default=None)
    address: Optional[str] = field(default=None)
    country: Optional[str] = field(default=None)
    social: Optional[list[str]] = field(default_factory=lambda: [])
