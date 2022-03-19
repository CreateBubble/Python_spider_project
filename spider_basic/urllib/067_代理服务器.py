# -*- coding: utf-8 -*-
# @File : 067_代理服务器.py
# @Author  : Bubble
# @Time    : 2022/3/19 12:07
# @Function:
# 1、访问国外站点
# 2、访问一些单位或团体内部资源
# 3、提高访问速度
# 4、隐藏真实ip，免受攻击
import urllib.request

url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
}

proxies = {
    'http': '124.205.155.155:9090'
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
with open('daili2.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
