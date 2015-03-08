# -*- coding: utf-8 -*-
import sys
import scrapy
from datetime import datetime
from scrapy.http import Request, FormRequest, TextResponse
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
from ..items import CgmhItem
#from scrapy.stats import Stats

class CgmhPsy(scrapy.Spider):
	name = "cgmhPsy"
	allowed_domains = ["org.tw"]
	start_urls = [
		"https://www.cgmh.org.tw/register/RMSTimeTable.aspx?dpt=13600A"
	]

	def parse(self, response):

		request = Request(response.url, callback = self.parse_table)
		yield request

	def parse_table(self, response):
		
		items = []
		sel = Selector(response)
		#print sel.extract()
		tables = sel.xpath('//table[@class="tableStyle"]/tr')
		print 'len of table = '+ str(len(tables))
		
		for t in range(len(tables)-1):
			##每個table看有幾個row
			table = tables[t+1]
			##print "list: " + str(t) + "," + table.extract()
			
			for n in table.xpath('.//td'):
				print n.extract()


'''
			for n in range(len(table)-1):
				print "n = " + str(n)

				##每個row看有幾行            
				tds = table[n+1].xpath('.//td')
				print "tds = " + str(len(tds))

				for day in range(len(tds)-2):
					print "day = " + str(day)
					item = NtuhItem()
					try:
						name = table[n+1].xpath('.//td')[day+2].xpath('.//font/text()').extract()
						if (name == []):
							continue
						
						item['name'] = name[0]
						item['hospital'] = 'ntuh'
						item['crawlTime'] = unicode(datetime.now().strftime("%Y%m%d %H:%M"))
						
						##區分成人及兒童
						if (t < 2):
							item['dept'] = 'PSY'
						else:
							item['dept'] = 'Chld_PSY'
						

						date = table[0].xpath('.//b/text()')[day+2].extract().split(" ")[0].split(".")
						date = str(int(date[0])+1911) + date[1] + date[2]
						item['date'] = date

						##區分時段
						if (t % 2 == 0):
							item['time'] = 'morning'
						else:
							item['time'] = 'afternoon'

						item['link'] = "https://reg.ntuh.gov.tw/webadministration/" + \
							table[n+1].xpath('.//td')[day+2].xpath('.//a/@href').extract()[0]
						
						yield Request(item['link'], callback = self.parse_shift, meta = {'item': item})                
						items.append(item)

					except Exception as e:
						pass
					#print item['name']
					
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
'''
