# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    排名 = scrapy.Field()
    电影名 = scrapy.Field()
