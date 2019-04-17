from django.shortcuts import render
from .mongo_db_helper import *


def companies(request):
    curr_page = request.GET.get('page', '1')
    curr_page = int(curr_page)

    # 获取总条数
    total_count = get_companies_count()
    # 每页条数
    page_rows = 10

    # 计算有多少页
    page_count = total_count // page_rows
    if total_count % page_rows > 0:
        page_count += 1

    if curr_page > 1:
        prev_page = curr_page - 1
    else:
        prev_page = 1

    if curr_page < page_count:
        next_page = curr_page + 1
    else:
        next_page = curr_page

    result = get_companies_by_page(curr_page - 1, page_rows)
    context = {'companies': result, 'total_count': total_count, 'page_count': page_count, 'curr_page': curr_page, 'prev_page': prev_page, 'next_page': next_page}

    return render(request, 'companies.html', context) 