
import os

import pymongo

client = pymongo.MongoClient()

db = client['u17']


def insert_commic(item):
    db.commic.insert_one(item)