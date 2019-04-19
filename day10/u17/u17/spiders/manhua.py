# -*- coding: utf-8 -*-
import scrapy
import json

from u17.items import U17Item, U17ChapterItem


class ManhuaSpider(scrapy.Spider):
    name = 'manhua'
    allowed_domains = ['www.u17.com']
    start_urls = ['http://www.u17.com/']

    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Host': 'www.u17.com',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        return headers

    # 构造请求
    def start_requests(self):
        url = 'http://www.u17.com/comic/ajax.php?mod=comic_list&act=comic_list_new_fun&a=get_comic_list'
        headers = self.get_headers()

        data = {
            'data[group_id]': 'no', 
            'data[theme_id]': 'no', 
            'data[is_vip]': 'no', 
            'data[accredit]': 'no', 
            'data[color]': 'no', 
            'data[comic_type]': 'no', 
            'data[series_status]': 'no', 
            'data[order]': '2', 
            'data[page_num]': '1', 
            'data[read_mode]': 'no'
        }

        for page in range(1, 500, 1):
            data['data[page_num]'] = str(page)
            yield scrapy.FormRequest(url=url, headers=headers, method='POST', formdata=data, callback=self.parse)


    # 解析响应	
    def parse(self, response):
        data_json = json.loads(response.text)
        result = data_json['comic_list']
        headers = self.get_headers()
        for data in result:
            item = U17Item()
            item['comic_id'] = data['comic_id']
            item['name'] = data['name']
            item['cover'] = data['cover']
            item['line2'] = data['line2']
            yield item

            # 爬取详细信息，构造请求
            # detali_url = 'http://www.u17.com/comic/%s.html' % item['comic_id']
            # yield scrapy.Request(url=detali_url, headers=headers, callback=self.detail_parse)


    def detail_parse(self, response):
        url = response.url
        comic_id = url.split('/')[-1].split('.')[0]
        result = response.selector.css('#chapter li')
        for data in result:
            item = U17ChapterItem()
            item['chapter_url'] = data.xpath('./a/@href').extract_first()
            text_list = data.xpath('.//text()').extract()
            item['title'] = ''.join([ text.strip() for text in text_list ])
            item['chapter_id'] = data.xpath('./a/@id').extract_first().split('_')[-1]
            item['comic_id'] = comic_id
            yield item