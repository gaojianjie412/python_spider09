
import requests
import json
from mongo_db_helper import *


def get_page(page):
    url = 'https://www.qichamao.com/cert-wall'
    headers = {
        "Referer": 'https://www.qichamao.com/person/hot',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host': 'www.qichamao.com'
    }
    data = {'page': str(page), 'pagesize': '9'}
    session = requests.Session()
    response = session.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return response.text


def main():
    for page in range(2, 200, 1):
        print(page)
        html = get_page(page)
        # print(html)
        json_data = json.loads(html)
        data_list = json_data['dataList']
        for item in data_list:
            print(item)
            insert_company(item)


if __name__ == '__main__':
    main()
