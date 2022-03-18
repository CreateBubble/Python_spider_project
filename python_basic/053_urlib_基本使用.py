# _*_ coding: utf-8 _*_
# @file : 053_urlib_基本使用.py
# @author : sunchuanfu
# @contact:s2271204754@163.com
# @time : 2022/3/17 19:56
# @Version：V 0.1
# @desc :

# 使用urlib来获取百度首页的源码
import urllib.request

# 1、定义一个url  你要访问的网站
url = 'http://www.baidu.com'

# 2、模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 3、获取响应中的页面的源码
# read()方法 返回的是字节形式的二进制数据
# 要将二进制的数据转换为字符串 解码
content = response.read().decode('utf-8')

# 4、打印数据
print(content)

