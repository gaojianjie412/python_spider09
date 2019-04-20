from django.shortcuts import render
from .mongodb_helper import *


def get_content(request):
    curr_page = int(request.GET.get('page', '1'))

    # 每页数据条数
    page_rows = 10
    # 所有数据的数量
    total_information = get_information_count()
    # 总页码
    total_page = total_information // page_rows
    if total_information % page_rows > 0:
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

    result = get_information_by_page(curr_page, page_rows)
    context = {'content': result, 'total_information': total_information, 'total_page': total_page,
               'curr_page': curr_page, 'prev_page': prev_page, 'next_page': next_page}
    return render(request, 'information.html', context)


