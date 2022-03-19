# -*- coding: utf-8 -*-
# @File : 071_获取百度网站的百度一下.py
# @Author  : Bubble
# @Time    : 2022/3/19 13:17
# @Function:

# 1、获取网页的源码
# 2、解析  解析的服务器响应的文件  etree.HTML
# 3、打印

import urllib.request
from lxml import etree

url = 'https://www.baidu.com'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应数据
content = response.read().decode('utf-8')

# 解析网页源码 来获取我们想要的数据
# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据 xpath的返回值是列表类型的数据
result = tree.xpath('//input[@id="su"]/@value')

print(result[0])
