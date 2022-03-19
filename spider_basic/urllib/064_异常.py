# -*- coding: utf-8 -*-
# @File : 064_异常.py
# @Author  : Bubble
# @Time    : 2022/3/19 11:15
# @Function:
import urllib.request
import urllib.error
url = 'https://blog.csdn.net/weixin_44096133/article/details/12344497'

url  = 'http://www.douban111.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

try:
    request = urllib.request.Request(url=url,headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级')
except urllib.error.URLError:
    print('系统还在升级。。。。。')