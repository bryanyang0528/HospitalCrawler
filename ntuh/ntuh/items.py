# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class NtuhItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    crawlTime = Field()
    hospital = Field()
    dept = Field()
    date = Field()
    time = Field()
    name = Field()
    link = Field()
    full = Field()

