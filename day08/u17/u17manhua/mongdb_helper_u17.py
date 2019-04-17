
import os

import pymongo

client = pymongo.MongoClient()

db = client['u17']


def insert_commic(item):
    db.commic.insert_one(item)


# 获取所有记录
def get_commics():
    result = db.commic.find({})
    return result


# 获取总记录数
def get_count():
    result = db.commic.count()
    return result


# 分页查询
def get_commics_by_page(page, page_rows):
    skip_rows = page * page_rows
    result = db.commic.find({}).sort('_id').skip(skip_rows).limit(page_rows)
    return result
