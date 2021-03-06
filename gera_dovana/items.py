# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GeraDovanaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    users = scrapy.Field()
    rating = scrapy.Field()
    votes = scrapy.Field()
    url = scrapy.Field()
