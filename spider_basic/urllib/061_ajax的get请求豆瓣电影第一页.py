# -*- coding: utf-8 -*-
# @File : 061_ajax的get请求豆瓣电影第一页.py
# @Author  : Bubble
# @Time    : 2022/3/18 21:14
# @Function:获取豆瓣电影第一页的内容并保存起来

import urllib.request

# get请求

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# 数据下载到本地
# open方法默认情况下使用的是gbk编码 如果我们想要保存汉字，需要在open中指定utf-8的编码格式
# encoding='utf-8'
# fp = open('douban.json','w', encoding='utf-8')
# fp.write(content)
with open('douban1.json','w',encoding='utf-8') as fp:
    fp.write(content)