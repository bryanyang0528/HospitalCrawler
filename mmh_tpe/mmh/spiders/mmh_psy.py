# -*- coding: utf-8 -*-
import sys
import scrapy
from datetime import datetime
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest, TextResponse
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
from ..items import NtuhItem
#from scrapy.stats import Stats

class MmhPSY(CrawlSpider):
    name = "mmhPSY"
    allowed_domains = ["org.tw"]
    start_urls = [
        "https://tpreg.mmh.org.tw/Dept.aspx?dept=21&Lang=C"
    ]

    rules = [
        Rule(SgmlLinkExtractor(allow = ('DrSch\.aspx\?dept=21&dr=\d')),
        callback = 'parse_table', follow = True)
    ]

    def parse_table(self, response):
        print(response.url)


