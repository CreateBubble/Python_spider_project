# -*- coding: utf-8 -*-
# @File : 083_handless.py
# @Author  : Bubble
# @Time    : 2022/3/19 21:13
# @Function:

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
#
# # path是你自己chrome浏览器的文件路径
# path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = path
#
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
#
# url = 'https://www.baidu.com'
#
# browser.get(url)
#
# browser.save_screenshot('baidu.png')

# 封装的handless
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

    # path是你自己chrome浏览器的文件路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser


browser = share_browser()

url = 'https://www.baidu.com'

browser.get(url)
