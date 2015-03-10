# -*- coding: utf-8 -*-

# Scrapy settings for cgmh project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cgmh'

SPIDER_MODULES = ['cgmh.spiders']
NEWSPIDER_MODULE = 'cgmh.spiders'

USER_AGENT = "Chrome/40.0.2214.111"
DOWNLOAD_DELAY = 0.25
#LOG_FILE = 'log.txt'

FEED_URI = 'export_cgmh.json'
FEED_FORMAT = 'json'
FEED_EXPORTERS = {
   'json': 'cgmh.pipelines.UnicodeJsonItemExporter'
}

