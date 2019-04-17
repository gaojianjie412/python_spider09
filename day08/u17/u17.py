
import requests
import json
from mongdb_helper import *


def get_page(page):
    url = 'http://www.u17.com/comic/ajax.php?mod=comic_list&act=comic_list_new_fun&a=get_comic_list'
    headers = {
        "Referer": 'http://www.u17.com/comic_list/th99_gr99_ca99_ss99_ob0_ac0_as0_wm0_co99_ct99_p1.html?order=2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host': 'www.u17.com'
    }
    data = {'data[group_id]': 'no',
            'data[theme_id]': 'no',
            'data[is_vip]': 'no',
            'data[accredit]': 'no',
            'data[color]': 'no',
            'data[comic_type]': 'no',
            'data[series_status]': 'no',
            'data[read_mode]': 'no',
            'data[order]': '2',
            'data[page_num]': str(page)}
    session = requests.Session()
    response = session.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return response.text


def main():
    for page in range(200, 417, 1):
        print(page)
        html = get_page(page)
        json_data = json.loads(html)
        data_list = json_data['comic_list']
        for item in data_list:
            print(item)
            insert_commic(item)


if __name__ == '__main__':
    main()
