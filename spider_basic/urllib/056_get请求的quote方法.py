# _*_ coding: utf-8 _*_
# @file : 056_get请求的quote方法.py
# @author : sunchuanfu
# @contact:s2271204754@163.com
# @time : 2022/3/18 11:35
# @Version：V 0.1
# @desc :
# A 65, a 97 0 48

# 需求 获取 https://www.baidu.com/s?ie=UTF-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6 周杰伦的网页源码

import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?ie=UTF-8&wd='

# 请求对象的定值是为了解决反爬的第一种手段

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

# 将周杰伦三个字变成unicode编码
# 我们需要依赖urllib.parse
name = urllib.parse.quote('周杰伦')

url = url + name

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的内容
content = response.read().decode('utf8')

# 打印内容
print(content)
