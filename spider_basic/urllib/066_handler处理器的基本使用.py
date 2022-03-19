# -*- coding: utf-8 -*-
# @File : 066_handler处理器的基本使用.py
# @Author  : Bubble
# @Time    : 2022/3/19 11:54
# @Function:

# 需求 使用hander访问百度，获取网页源码

import urllib.request


url = 'http://www.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

# handler   build_opener    open

# 获取handler对象
handler = urllib.request.HTTPHandler()

# 获取opener对象
opener = urllib.request.build_opener(handler)

# 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)