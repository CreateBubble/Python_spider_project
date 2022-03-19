# -*- coding: utf-8 -*-
# @File : 076_bs4爬取星巴克数据.py
# @Author  : Bubble
# @Time    : 2022/3/19 17:26
# @Function:
import urllib.request

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url=url)

content = response.read().decode('utf-8')

from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# //ul[@class="grid padded-3 product"]//strong/text()
name_list = soup.select('ul[class="grid padded-3 product"] strong')

for name in name_list:
    print(name.get_text())