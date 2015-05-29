#!/bin/bash
# Date:2015-03-10
# Version:0.1

echo "*****running scrapy for ntuh*****"
scrapy crawl ntuhPSY
scrapy crawl ntuhURO
scrapy crawl ntuhSURG
scrapy crawl ntuhORTH
scrapy crawl ntuhONC
scrapy crawl ntuhNEUR
scrapy crawl ntuhMET
scrapy crawl ntuhENT
exit 0
