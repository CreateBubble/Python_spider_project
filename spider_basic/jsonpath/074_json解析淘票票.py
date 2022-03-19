# -*- coding: utf-8 -*-
# @File : 074_json解析淘票票.py
# @Author  : Bubble
# @Time    : 2022/3/19 16:23
# @Function:

import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1647678294792_113&jsoncallback=jsonp114&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1647678294792_113&jsoncallback=jsonp114&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'miid=58923378041865775; enc=GZfP6y5wQCTH9pJMOBYU8lgHjwUKOyLY1JP6npMylzJdQnO18yuf25ba5Fj11a37dTlIfxqvqkcEntTWyB8CJgnSuUbpGH%2B5y3b4YUB7LL1lUmbI7f0cc%2B8hTPTT8CQm; t=896e15ec9ade22c509ac90df6aa2925a; thw=cn; cna=bQOuGur93i8CASRxI8AaVSo0; cookie2=1b5648a9d3c6196791c3057f917d831b; v=0; _tb_token_=e6b659e353766; xlly_s=1; l=eBPf2CvILSuprCCMBO5Cnurza77OiIOb4oVzaNbMiInca1oRTFGcCNCnPgJM7dtjgtCcFetrzU4ZdRLHR3ji5c0c07kqm0-m3xvO.; tfstk=ckWGBuflJ1RsDhRhNR91YrbsbaadafNw5tWFLTENlt0DFzXebsYmTbJT9kYTPPlf.; isg=BKurfTLrTce6UpGX4rFoPoyEOs-VwL9CchXaDB0piupBvMsepZGZkgRSFvzSmBc6',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 切割split()
content = content.split('(')[1].split(')')[0]

with open('074_json解析淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

#
obj = json.load(open('074_json解析淘票票.json', 'r', encoding='utf-8'))

city_list = jsonpath.jsonpath(obj, '$..regionName')

print(city_list)
