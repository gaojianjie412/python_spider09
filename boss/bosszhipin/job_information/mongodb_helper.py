
import pymongo

client = pymongo.MongoClient()

db = client['boss']


# 一条一条数据插入
def insert_information(item):
    db.information.insert_one(item)


# 获得所有数据
def get_information():
    result = db.information.find({})
    return result


# 获得所有数据的数量
def get_information_count():
    return db.information.count()


# 分页查询
def get_information_by_page(page, page_rows):
    skip_pages = page * page_rows
    result = db.information.find({}).sort('_d').skip(skip_pages).limit(page_rows)
    return result
