# -*- coding: utf-8 -*-

# Scrapy settings for aquarius project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'aquarius'

SPIDER_MODULES = ['aquarius.spiders']
NEWSPIDER_MODULE = 'aquarius.spiders'
ITEM_PIPELINES = {
    'aquarius.pipelines.AquariusPipeline': 2
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'aquarius (+http://www.yourdomain.com)'
