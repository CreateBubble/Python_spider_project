# -*- coding: utf-8 -*-
# @File : 079_元素定位.py
# @Author  : Bubble
# @Time    : 2022/3/19 20:33
# @Function:
from selenium import webdriver

#
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

# 元素定位
# 根据Id来找到对象
button = browser.find_element_by_id('su')

# 根据标签属性的属性值
button1 = browser.find_element_by_name('wd')

# 根据xpath语句获取对象
button2 = browser.find_elements_by_xpath('//input[@id="su"]')

# 根据标签名字来获取对象
button3 = browser.find_element_by_tag_name('input')

# 使用的是bs4的语法来获取对象
button4 = browser.find_elements_by_css_selector('#su')

# 使用连接本文
button5 = browser.find_element_by_link_text('直播')
