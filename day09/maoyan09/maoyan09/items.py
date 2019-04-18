# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Maoyan09Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    actor = scrapy.Field()
    release_time = scrapy.Field()
    cover_url = scrapy.Field()

