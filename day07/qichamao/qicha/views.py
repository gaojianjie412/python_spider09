from django.http import JsonResponse
from django.shortcuts import render
from .mongo_db_helper import *
from collections import Counter


# 返回json数据
def report_data(request):
    # json_data = {'x': ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
    #              'y': [34, 12, 56, 89, 98, 100, 120]}
    comics = get_comics()
    category_list = []
    for comic in comics:
        category = comic['line2']
        category_list.append(category)

    c = dict(Counter(category_list))
    json_data = {'x': list(c.keys()), 'y': list(c.values())}
    return JsonResponse(json_data)


def report(request):
    context = {}
    return render(request, 'report.html', context)


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

