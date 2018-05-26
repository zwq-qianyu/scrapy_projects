# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PybookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    pre_price = scrapy.Field()
    now_price = scrapy.Field()
    publish = scrapy.Field()
    pic = scrapy.Field()
    detail = scrapy.Field()