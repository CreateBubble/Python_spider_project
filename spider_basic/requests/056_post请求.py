# -*- coding: utf-8 -*-
# @File : 056_post请求.py
# @Author  : Bubble
# @Time    : 2022/3/20 10:36
# @Function:
import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

data = {
    'kw': 'eye'
}

# url请求地址
# data 请求参数
# keargs 字典
response = requests.post(url=url, data=data, headers=headers)

content = response.text

import json

obj = json.loads(content)

print(obj)

# 总结
# 1、post请求 是不需要编解码
# 2、post请求的参数是data
# 3、不需要请求对象的定制