# -*- coding: utf-8 -*-
import scrapy
from meizitu.items import MeizituItem


class PictureSpider(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['http://www.mzitu.com/']

    def parse(self, response):
        result = response.selector.xpath('//ul[@id="pins"]')
        detail_urls = result.css('li a::attr(href)').extract()
        names = result.css('a img::attr(alt)').extract()
        img_urls = result.css('a img::attr(src)').extract()
        for i in range(len(detail_urls)):
            item = MeizituItem()
            item['detail_url'] = detail_urls[i]
            item['name'] = names[i]
            item['img_url'] = img_urls[i]
            yield item
