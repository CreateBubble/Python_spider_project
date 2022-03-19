# -*- coding: utf-8 -*-
# @File : 078_基本使用.py
# @Author  : Bubble
# @Time    : 2022/3/19 20:07
# @Function:
# 1、web应用程序测试的工具
# 2、测试直接运行在浏览器中，像真正用户在操作一样
# 3、支持通过各种driver驱动真实的浏览器完成测试
# 4、支持无界面浏览器操作
# 模拟浏览器功能，自动执行网页中的js代码实现动态加载
# 1、导入slenium
from selenium import webdriver
# 2、创建浏览器操作对象
path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

# 3、访问网站
url = 'https://www.jd.com'

browser.get(url)
# page_source获取网页源码
content = browser.page_source
print(content)