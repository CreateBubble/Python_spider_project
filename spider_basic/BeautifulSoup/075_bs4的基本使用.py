# -*- coding: utf-8 -*-
# @File : 075_bs4的基本使用.py
# @Author  : Bubble
# @Time    : 2022/3/19 16:42
# @Function:
# 和lxml一样是一个html解析器 主要功能是解析和提取数据
# 优点：接口设计人性化、使用方便
# 缺点：效率没有lxml高
from bs4 import BeautifulSoup

# 解析本地文件 来讲bs4的基础语法进行讲解
# 默认打开文件的编码格式是gbk 所以打开文件的时候需要指定编码
soup = BeautifulSoup(open('075_bs4的基本使用.html', encoding='utf-8'), 'lxml')

# 根据标签的名字来查找节点
# 找到的是第一个符合条件的数据
print(soup.a)
# 获取标签的属性和属性值
print(soup.a.attrs)

# bs4的一些函数
# 1、find
# 返回的是一个符合条件的数据
print(soup.find('a'))
# 根据title的值找到对应的标签对象
print(soup.find('a', title='a2'))
# 根据class的值找到对应的标签对象，注意class需要添加_
print(soup.find('a', class_='a1'))

# 2、fina_all 返回的是一个列表，并且返回了所有的a标签
print(soup.find_all('a'))
# 如果要返回多个标签的数据，需要在find_all中添加的是列表的数据
print(soup.find_all(['a','span']))
# limit的作用 是查找前几个数据
print(soup.find_all('li', limit=2))
# 3、select 推荐
# select方法 返回的多个数据的列表
print(soup.select('a'))
# 可以通过.代表class 类选择器
print(soup.select('.a1'))
# id选择器
print(soup.select('#l1'))

# 属性选择器----通过属性来寻找对应的标签
# 查找到li标签中有id的标签
print(soup.select('li[id]'))

# 查找到li标签中id为l2的标签
print(soup.select('li[id="l2"]'))

# 层级选择器
# 后代选择器
# 找到是div下边的li
print(soup.select('div li'))

# 子代选择器
# 某标签的第一级子标签
# 注意：很多的计算机编程语言中，如果不加空格不会输出内容 但在bs4中不会报错
print(soup.select('div > ul >li'))

# # 找到a标签和li标签的所有的对象
print(soup.select('a,li'))

# 节点信息
#   获取节点内容
# 如果标签对象中只有内容 那么string 和get_text()都可以使用
# 如果标签对象中除了内容还有标签 只能用get_text()获取数据
# 推荐使用get_text()
obj = soup.select('#d1')[0]
print(obj.string)
print(obj.get_text())

# 节点的属性
obj = soup.select('#p1')[0]
# name是标签的名字
print(obj.name)
# attars将属性值作为一个字典返回
print(obj.attrs)

# 获取节点的属性
obj = soup.select('#p1')[0]
# 推荐
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])