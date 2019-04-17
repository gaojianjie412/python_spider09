
import pymongo

client = pymongo.MongoClient()

db = client['qichamao']

def insert_company(item):
	db.company.insert_one(item)


# 取所有记录
def get_companies():
	result = db.company.find({})
	return result


# 取总记录数
def get_companies_count():
	return db.company.count()


# 分页查询
def get_companies_by_page(page, page_rows):
	skip_rows = page * page_rows
	result = db.company.find({}).sort('_d').skip(skip_rows).limit(page_rows)
	return result
