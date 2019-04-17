
import pymongo

client = pymongo.MongoClient()

db = client['qichamao']


def insert_company(item):
    db.company.insert_one(item)
