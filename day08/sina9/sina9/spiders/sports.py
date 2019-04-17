# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from sina9.items import Sina9Item


class SportsSpider(scrapy.Spider):
    name = 'sports'
    allowed_domains = ['sports.sina.com.cn']
    start_urls = ['http://sports.sina.com.cn/']

    def parse(self, response):
        etree_html = etree.HTML(response.text)
        titles = etree_html.xpath('//h3[@class="ty-card-tt"]//text()')
        for title in titles:
            item = Sina9Item()
            item['title'] = title
            yield item
