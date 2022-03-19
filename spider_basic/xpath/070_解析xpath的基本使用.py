# -*- coding: utf-8 -*-
# @File : 070_解析xpath的基本使用.py
# @Author  : Bubble
# @Time    : 2022/3/19 12:47
# @Function:
from lxml import etree
# xpath解析
# 1、本地文件                                          etree.parse
# 2、服务器响应的数据 response.read().decode('utf-8')   etree.HTML()

# xpath解析本地文件
tree = etree.parse('070_解析xpath的基本使用.html')


#     <ul>
#         <li id="l1" class="c1">北京</li>
#         <li id="l2">上海</li>
#         <li>深圳</li>
#         <li>武汉</li>
#     </ul>

# //找子孙结点  /找子结点
# 查找ul下面的li
li_list = tree.xpath('//body//ul/li')
# 查找所有由id属性的li标签
li_list2 = tree.xpath('//ul/li[@id]/text()')
# 找到id为l1的li标签
li_list3 = tree.xpath('//ul/li[@id="l2"]/text()')
# 找到id为l1标签的class属性值
li = tree.xpath('//ul/li[@id="l1"]/@class')
# 查找id中包含l的li标签 模糊查询
li2 = tree.xpath('//ul/li[contains(@id,"l")]/text()')
# 查找id的值以l开头的li标签  以...为开头
li3 = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
# 查询id为l1和class为c1的标签  and逻辑运算
li4 = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
# 查询id为l1或id为l2的标签  or逻辑运算  |
li5 = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text() ')
li6 = tree.xpath('//ul/li[@id="l1" or @id="l2"]/text()')

# 判断列表的长度
print(li_list)
print(li_list2)
print(li_list3)
print(li)
print(li2)
print(li3)
print(li4)
print(li5)
print(li6)