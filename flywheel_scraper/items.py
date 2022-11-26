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
    url: str = field(default=None)
    business_name: str = field(default=None)
    website: str = field(default=None)
    detail: str = field(default=None)
    address: str = field(default=None)
    country: str = field(default=None)
    social: list[str] = field(default_factory=lambda: [])
    facebook: str = field(default=None)
    instagram: str = field(default=None)
    linkedin: str = field(default=None)
    twitter: str = field(default=None)
