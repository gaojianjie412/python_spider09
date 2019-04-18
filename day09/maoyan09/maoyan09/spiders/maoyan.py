# -*- coding: utf-8 -*-
import scrapy
from maoyan09.items import Maoyan09Item


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/4']

    # 构造请求
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        for page in range(10):
            url = 'https://maoyan.com/board/4?offset=%d' % (page * 10)
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    # 解析响应
    def parse(self, response):
        data_list = response.selector.css('dl.board-wrapper dd')
        for data in data_list:
            item = Maoyan09Item()
            # 电影名称
            item['title'] = data.css('p.name a::text').extract_first()
            # 演员
            item['actor'] = data.css('p.star::text').extract_first().strip()
            # 上映时间
            item['release_time'] = data.css('p.releasetime::text').extract_first()
            # 封面图片
            item['cover_url'] = data.css('img.board-img::attr(data-src)').extract_first()
            yield item
