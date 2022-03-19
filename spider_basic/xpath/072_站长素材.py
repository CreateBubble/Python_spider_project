# -*- coding: utf-8 -*-
# @File : 072_站长素材.py
# @Author  : Bubble
# @Time    : 2022/3/19 13:30
# @Function:获取前十页的地址
# 请求对象的定制
# 获取网页的源码
# 下载
import urllib.request
from lxml import etree
# https://sc.chinaz.com/tupian/qinglvtupian.html   1
# https://sc.chinaz.com/tupian/qinglvtupian_2.html


def create_request(page):

    if(page == 1):
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    # 下载图片
    # urllib.request.urlretrieve('图片地址','文件的名字')
    tree = etree.HTML(content)

    name_list = tree.xpath('//div[@id="container"]//a//img/@alt')
    # 一般涉及到图片的页面，一般采用懒加载
    src_list = tree.xpath('//div[@id="container"]//a//img/@src2')

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename='./loveimage/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))

    for page in range(start_page, end_page+1):
        # 请求对象的定制
        request = create_request(page)
        # 获取网页的源码
        content = get_content(request)
        # 下载
        down_load(content)
