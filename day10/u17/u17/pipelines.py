# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo
from mongoengine import *
from scrapy import Request
from scrapy.exceptions import DropItem


from scrapy.pipelines.images import ImagesPipeline
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

# from u17.models import U17
from u17.mongo_models import ComicStore, ComicChapter


class U17PyMysqlPipeline(object):
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    # 从配置文件读取mysql配置信息
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            username=crawler.settings.get('MYSQL_USERNAME'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            )

    # 创建蜘蛛的时候会自动调用
    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    # 关闭蜘蛛的时候调用
    def close_spider(self, spider):
        self.db.close()

    # 处理item数据，插入数据库
    def process_item(self, item, spider):
        sql = ''
        param = None
        if item.collection == 'comic':
            sql = 'insert into comic (comic_id, name, cover, line2) values (%s, %s, %s ,%s)'
            param = (item['comic_id'], item['name'], item['cover'], item['line2'])
        else:
            sql = 'insert into comic_chapter (chapter_id, chapter_url, title, comic_id) values (%s, %s, %s, %s)'
            param = (item['chapter_id'], item['chapter_url'], item['title'], item['comic_id'])

        self.cursor.execute(sql, param)
        self.db.commit()
        return item


# sqlalchemy保存
class U17SqlalchemyPipeline(object):
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

        self.engine = create_engine("mysql+pymysql://%s:%s@%s/%s?charset=utf8" % (self.username, self.password, self.host, self.database), max_overflow=5)
        print("----------**********carmack**********")
        print(self.engine)
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = None


    # 从配置文件读取mysql配置信息
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            username=crawler.settings.get('MYSQL_USERNAME'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            )

    # 创建蜘蛛的时候会自动调用
    def open_spider(self, spider):
        self.session = self.session_maker()

    # 关闭蜘蛛的时候调用
    def close_spider(self, spider):
        self.session.close()

    # 处理item数据，插入数据库
    def process_item(self, item, spider):
        u17 = U17()
        u17.comic_id = item['comic_id']
        u17.name = item['name']
        u17.cover = item['cover']
        u17.line2 = item['line2']
        self.session.add(u17)
        self.session.commit()

        return item


# pymongo保存
class U17PyMongoPipeline(object):
    def __init__(self, uri, database):
        self.uri = uri
        self.database = database

    # 从配置文件读取mysql配置信息
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            uri=crawler.settings.get('MONGO_URI'),
            database=crawler.settings.get('MONGO_DB')
            )

    # 创建蜘蛛的时候会自动调用
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client[self.database]

    # 关闭蜘蛛的时候调用
    def close_spider(self, spider):
        self.client.close()

    # 处理item数据，插入数据库
    def process_item(self, item, spider):
        collection = item.collection
        self.db[collection].insert_one(dict(item))
        return item


# mongoengine保存
class U17MongoEnginePipeline(object):
    def __init__(self, uri, database):
        self.uri = uri
        self.database = database

    # 从配置文件读取mysql配置信息
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            uri=crawler.settings.get('MONGO_URI'),
            database=crawler.settings.get('MONGO_DB')
            )

    # 创建蜘蛛的时候会自动调用
    def open_spider(self, spider):
        self.connection = connect(self.database)

    # 关闭蜘蛛的时候调用
    def close_spider(self, spider):
        self.connection.close()

    # 处理item数据，插入数据库
    def process_item(self, item, spider):
        if item.collection == 'comic':
            comic = ComicStore()
            comic.comic_id = item['comic_id']
            comic.name = item['name']
            comic.cover = item['cover']
            comic.line2 = item['line2']
            comic.save()
        else:
            comic_chapter = ComicChapter()
            comic_chapter.comic_id = item['comic_id']
            comic_chapter.chapter_id = item['chapter_id']
            comic_chapter.chapter_url = item['chapter_url']
            comic_chapter.title = item['title']
            comic_chapter.save()

        return item


# 图片保存
class U17ImagePipeline(ImagesPipeline):

    # 图片文件命名
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    # 判断文件是否下载成功
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item


    # 构建图片下载请求
    def get_media_requests(self, item, info):
        yield Request(item['cover'])

