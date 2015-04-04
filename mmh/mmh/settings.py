# -*- coding: utf-8 -*-

# Scrapy settings for ntuh project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mmh_tpe'

SPIDER_MODULES = ['mmh.spiders']
NEWSPIDER_MODULE = 'mmh.spiders'
USER_AGENT = "Chrome/40.0.2214.111"
DOWNLOAD_DELAY = 0.25
#LOG_FILE = 'log.txt'

FEED_URI = 'export.json'
FEED_FORMAT = 'json'
FEED_EXPORTERS = {
   'json': 'mmh.pipelines.UnicodeJsonItemExporter'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ntuh (+http://www.yourdomain.com)'
