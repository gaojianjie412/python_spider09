
import pymongo

client = pymongo.MongoClient()

db = client['boss']


# 一条一条数据插入
def insert_information(item):
    db.information.insert_one(item)


# 获得所有数据
def get_information():
    db.information.find({})