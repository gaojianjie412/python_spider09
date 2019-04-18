# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class U17Item(scrapy.Item):
    collection = table = 'comic'
    name = scrapy.Field()
    cover = scrapy.Field()
    comic_id = scrapy.Field()
    line2 = scrapy.Field()


class U17ChapterItem(scrapy.Item):
    collection = table = 'comic_chapter'
    comic_id = scrapy.Field()
    chapter_id = scrapy.Field()
    chapter_url = scrapy.Field()
    title = scrapy.Field()

