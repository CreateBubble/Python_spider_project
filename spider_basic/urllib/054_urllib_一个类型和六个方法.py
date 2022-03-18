# _*_ coding: utf-8 _*_
# @file : 054_urllib_一个类型和六个方法.py
# @author : sunchuanfu
# @contact:s2271204754@163.com
# @time : 2022/3/17 20:08
# @Version：V 0.1
# @desc :
import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response 是HTTPResponse类型
# print(type(response))
# 按照 个字节去读
# 1、read()
# 返回多少个字节

# 读取一行
# 2、readline（）

# 按行读，读所有
# 3、readlines()

# 返回状态码
# 4、getcode()

# 返回url地址
# 5、geturl

# 返回 状态信息
# 6、getheaders()

