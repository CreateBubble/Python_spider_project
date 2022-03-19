# -*- coding: utf-8 -*-
# @File : 073_jsonpath.py
# @Author  : Bubble
# @Time    : 2022/3/19 15:59
# @Function:
import json
import jsonpath

obj = json.load(open('073_jsonpath.json', 'r', encoding='utf-8'))

# 书店所有书的作者
author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')

# 所有的作者
author_list1 = jsonpath.jsonpath(obj, '$..author')

# store下面的所有元素
tag_list = jsonpath.jsonpath(obj, '$.store.*')

# store下所有东西的price
price_list = jsonpath.jsonpath(obj, '$.store..price')

# 第三本
book = jsonpath.jsonpath(obj, '$..book[2]')

# 最后一本书
end_book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')

# 前两本书
book_list = jsonpath.jsonpath(obj, '$..book[:2]')

# 条件过滤需要在()前边添加?
# 过滤所有包含版本号的书
book_list1 = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')

# 哪本书超过了10块钱
book_list2 = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(book_list2)

















