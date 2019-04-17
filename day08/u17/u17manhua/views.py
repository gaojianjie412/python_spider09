from django.shortcuts import render
from .mongdb_helper_u17 import *


def commics(request):
    curr_page = request.GET.get('page', '1')
    curr_page = int(curr_page)
    # 获取总条数
    total_count = get_count()
    # 每页条数
    page_rows = 10
    # 计算有多少页
    total_page = total_count // page_rows
    if total_count % page_rows > 0:
        total_page += 1
    # 上一页
    if curr_page > 1:
        prev_page = curr_page - 1
    else:
        prev_page = 1

    # 下一页
    if curr_page < total_page:
        next_page = curr_page + 1
    else:
        next_page = curr_page

    result = get_commics_by_page(curr_page - 1, page_rows)
    context = {'commics': result, 'total_page': total_page, 'total_count': total_count,
               'curr_page': curr_page, 'prev_page': prev_page, 'next_page': next_page}
    return render(request, 'commics.html', context)
