# -*- coding: utf-8 -*-
# @File : 080_元素信息.py
# @Author  : Bubble
# @Time    : 2022/3/19 20:45
# @Function:
from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'http://www.baidu.com'
browser.get(url)

input = browser.find_element_by_id('su')
# 获取属性
print(input.get_attribute('class'))
# 获取标签名
print(input.tag_name)

# 获取元素文本
a = browser.find_element_by_link_text('新闻')
print(a.text)
