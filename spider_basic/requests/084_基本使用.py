# -*- coding: utf-8 -*-
# @File : 084_基本使用.py
# @Author  : Bubble
# @Time    : 2022/3/20 10:21
# @Function:
import requests

url = 'http://wwww.baidu.com'

response = requests.get(url=url)

# 一个类型和六个属性
# Response类型
print(type(response))

# 设置响应的编码模式
response.encoding = 'utf-8'

# 以字符串的形式返回网页源码
print(response.text())

# 返回一个url地址
print(response.url)

# 返回的是二进制的数据
print(response.content)

# 返回响应的状态码
print(response.status_code)

# 返回的是响应头
print(response.headers)
