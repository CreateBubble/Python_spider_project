# -*- coding: utf-8 -*-
# @file : 060.py
# @Author  : Bubble
# @Time    : 2022/3/18 12:42
# @Function: urlencode方法：多个参数时

# https://www.baidu.com/s?wd=周杰伦&sex=男
import urllib.request
import urllib.parse


# 获取
base_url = 'http://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾'
}

new_data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url + new_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)