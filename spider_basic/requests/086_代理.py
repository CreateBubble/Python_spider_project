# -*- coding: utf-8 -*-
# @File : 086_代理.py
# @Author  : Bubble
# @Time    : 2022/3/20 10:49
# @Function:
import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
}

data = {
    'wd': 'ip'
}

proxy = {
    'http': '103.39.214.69:8118'
}

response = requests.get(url=url, params=data, headers=headers, proxies = proxy)

content = response.text

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)