# -*- coding: utf-8 -*-
# @File : 059_post请求百度翻译.py
# @Author  : Bubble
# @Time    : 2022/3/18 13:01
# @Function: post请求

import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

data = {
    'kw': 'spider'
}

# post请求的参数，必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数不会拼接到url后边，而是需要放在请求对象定制的参数中
request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 字符串-》json对象
import json
obj = json.loads(content)
print(obj)

# post请求方式的参数 必须编码 data = urllib.parse.urlencode(data)
# 编码之后 必须调用encode方法 data = urllib.parse.urlencode(data).encode('utf-8')
# 参数是放在请求对象定制的方法中 request = urllib.request.Request(url=url, data=data, headers=headers)