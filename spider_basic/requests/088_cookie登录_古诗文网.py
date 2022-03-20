# -*- coding: utf-8 -*-
# @File : 088_cookie登录_古诗文网.py
# @Author  : Bubble
# @Time    : 2022/3/20 10:55
# @Function:

# 通过登录，进入主界面

# 通过找登录接口我们发现 登录的时候需要的参数很多
# __VIEWSTATE: XcqSqFeAW1ust103oQ6Eh0TmP6oyhKlwbANUL0PNGKVycbGC3h96ofcCH0L4PaeT/54AwCRtbUrcb1tpngVOsCE7x3E7VqKhd6yBn4lSGoByMy7OYPj7UL602qA=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 17861502791
# pwd: PygerASAFASF
# code: DHLS
# denglu: 登录

# 我们观察到 __VIEWSTATE __VIEWSTATEGENERATOR code是一个可以变化的量

# 难点1、__VIEWSTATE      __VIEWSTATEGENERATOR  一般情况下看不到的数据都是在界面的源代码中
# 我们观察到这两个数据在页面的源码中,我们需要获取页面源码进行解析就可以获取了
#   2、验证码

import requests

# 登录界面url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

# 获取页面的源码
response = requests.get(url = url, headers = headers)
content = response.text

# 解析页面源码 获取__VIEWSTATE      __VIEWSTATEGENERATOR
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# 获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取__VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'http://so.gushiwen.cn' + code

# 有坑
# import urllib.request
# urllib.request.urlretrieve(url=url, filename='code.jpg')
# requests中有一个方法 session 通过session的返回值 就能使用请求变成一个对象

session = requests.session()
# 验证码url内容
response_code = session.get(code_url)
# 注意此时要使用二进制数据 因为我们要使用的是图片的下载
content_code = response_code.content
# wb模式就是将二进制数据写入文件
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)



# 获取验证码的图片之后 下载到本地 然后观察验证码
# 观察之后 然后在控制台输入这个验证码 就可以将这个值给code参数 就可以登录

code_name = input('请输入你的验证码')

# 点击登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '17861502791',
    'pwd': 'Pygery36',
    'code': code_name,
    'denglu': '登录',
}

response_post = session.post(url=url_post, headers=headers, data=data_post)

content_post = response_post.text

with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(content_post)

# 难点
# 1、隐藏域
# 2、验证码