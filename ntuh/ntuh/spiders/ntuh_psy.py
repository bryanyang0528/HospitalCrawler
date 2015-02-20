# -*- coding: utf-8 -*-
import sys
import scrapy
from scrapy.http import Request, FormRequest, TextResponse
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
from ..items import NtuhItem

class NtuhPsy(scrapy.Spider):
    name = "ntuhPsy"
    allowed_domains = ["gov.tw"]
    start_urls = [
        "https://reg.ntuh.gov.tw/webadministration/DoctorTable.aspx?Dept=PSYC&Hosp=T0&SubDeptCode=&isSubDept=N&week=1"
    ]

    def parse(self, response):

        request = Request(response.url, callback = self.parse_table)
        yield request

    def parse_table(self, response):
        
        items = []
        sel = Selector(response)
        table1 = sel.xpath('//table[@id="Table1"]/tr')
        #print table1.extract()
        print 'len of table1 = '+ str(len(table1))

        for day in range(7):
            for n in range(len(table1)-1):
                item = NtuhItem()
                name = table1[n+1].xpath('.//td')[day+2].xpath('.//font/text()').extract()
                #print item['name']
                if (name == []):
                    continue
                item['name'] = name[0]
                item['hospital'] = 'ntuh'
                item['dept'] = 'PSY'
                item['date'] = table1[0].xpath('.//b/text()')[day+2].extract().split(" ")[0]
                item['time'] = 'morning'
                item['link'] = "https://reg.ntuh.gov.tw/webadministration/" + \
                    table1[n+1].xpath('.//td')[day+2].xpath('.//a/@href').extract()[0]
                yield Request(item['link'], callback = self.parse_shift, meta = {'item': item})                
                items.append(item)
        #return items

    def parse_shift(self, response):

        item = response.meta['item']
        isFull = Selector(response).xpath('//table[@id= "DataTable"]/tr')[1].\
            xpath('.//font/text()').extract()[0].strip()

        if (isFull == u'名額已滿'):
            item['full'] = u'名額已滿'
        else:
            item['full'] = u'可掛號'

        return item

##output format

#hospital dept date time name

