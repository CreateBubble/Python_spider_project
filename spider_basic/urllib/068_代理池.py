# -*- coding: utf-8 -*-
# @File : 068_代理池.py
# @Author  : Bubble
# @Time    : 2022/3/19 12:22
# @Function:
import random
import urllib.request

proxies_pool = [
    {'http': '121.13.252.60:41564'},
    {'http': '47.92.234.75:80'},
]

proxies = random.choice(proxies_pool)

url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 获取handler对象
handler = urllib.request.ProxyHandler(proxies=proxies)
# 获取opener对象
opener = urllib.request.build_opener(handler)
# 调用open方法
response = opener.open(request)
# 获取响应信息
content = response.read().decode('utf-8')
# 保存
with open('dailipool.html', 'w', encoding='utf-8') as fp:
    fp.write(content)