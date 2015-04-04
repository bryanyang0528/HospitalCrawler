# -*- coding: utf-8 -*-
import sys
import re
import time
import scrapy
from datetime import datetime
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request, FormRequest, TextResponse
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
from ..items import MmhItem
#from scrapy.stats import Stats

class Mmhtpe(CrawlSpider):
    name = "mmhtpe"
    allowed_domains = ["org.tw"]
    start_urls = [
        "https://tpreg.mmh.org.tw/default.aspx?Lang=C"    
        ]

    rules = [
        Rule(LinkExtractor(allow = (u'Dept\.aspx\?dept=\d+')),
        follow = True),

        Rule(LinkExtractor(allow = ('DrSch\.aspx\?dept=.*&dr=\d+')),
        callback = 'parse_table', follow = True)
     ]

    def parse_table(self, response):
        items = []
        sel = Selector(response) 
        dept = re.sub("[\d+()]", "", sel.xpath('//table[@id="tblSch"]//tr[@class="title"]//span/text()')[0].extract().split(" ")[0])
        #print 'dept= ' + dept
        tables = sel.xpath('//table[@id="tblSch"]//tr/td/a')
        #print tables.extract()

        for table in tables:

            item = MmhItem()
            #print 'table = ' + table.extract()
            item['link'] = 'https://tpreg.mmh.org.tw/' + table.xpath('.//@href')[0].extract()
            
            try:
                full = table.xpath('.//font/text()').extract()
                if (len(full) == 2):
                    if (full[0] == u'滿號'):
                        item['full'] = full[0] 
                    item['outpatient'] = full[1]
                elif (len(full) == 1):
                    if (full[0] == u'滿號'):
                        item['full'] = full[0]
                    else:
                        item['outpatient'] = full[0]
                        item['full'] = '可掛號'
                else:
                    item['full'] = '可掛號'
            except:
                item['full'] = '可掛號'

            yield Request(item['link'], callback = self.parse_Drtable, meta = {'item': item}) 
            items.append(item)

    def parse_Drtable(self, response):
        #print(response.url)
        
        item = response.meta['item']
        sel = Selector(response)
        #print sel.extract()

        item['crawlTime'] = unicode(datetime.now().strftime("%Y%m%d %H:%M"))
        item['hospital'] = 'mmh_tpe'
        item['name'] = re.sub('[\d+()]', '', sel.xpath('//td[@class="content"]/text()')[3].extract())
        item['link'] = response.url
        item['dept'] = re.sub('[\d+()]', '', sel.xpath('//td[@class="content"]/text()')[2].extract().strip())

        date = sel.xpath('//td[@class="content"]/text()')[1].extract().split(' ')[0]
        #print 'date= '+ date
        dateFormat = '%Y/%m/%d'
        date = time.strptime(date, dateFormat)
        item['date'] = time.strftime("%Y%m%d", date)
        
        itemTime = sel.xpath('//td[@class="content"]/text()')[1].extract().split(' ')[2].strip()
   
        if (itemTime == u'上午'):
            item['time'] = 'morning'

        if (itemTime == u'下午'):
            item['time'] = 'afternoon'
        
        if (itemTime == u'夜診'):
            item['time'] = 'evening' 

        return item

    