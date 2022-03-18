# _*_ coding: utf-8 _*_
# @file : 057_请求对象的定制.py
# @author : sunchuanfu
# @contact:s2271204754@163.com
# @time : 2022/3/18 11:17
# @Version：V 0.1
# @desc :

import urllib.request

url = 'https://www.baidu.com'

# url组成
# http/https      www.baidu.com   80/443
# 协议                主机       端口号     路径     参数
# http  80
# https 443
# mysql 3306

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

# 因为urlopen中不能存储字典，所有Headers不能传入
# 请求对象定制
# 注意 因为参数顺序问题，不能写url和headers中间还有data,所有要使用关键字传参、
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)