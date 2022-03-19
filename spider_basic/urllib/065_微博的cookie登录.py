# -*- coding: utf-8 -*-
# @File : 065_微博的cookie登录.py
# @Author  : Bubble
# @Time    : 2022/3/19 11:23
# @Function:数据采集的时候，需要绕过登录进入某个界面
# 个人信息界面是utf-8 但是还是报错了，因为并没有进入个人登录界面 而是选择了跳转到了登录界面
# 那么登录界面不是utf-8 所以报错

import urllib.request

url = 'https://weibo.com/u/6426305588'
# cookie携带着你的登录信息 如果有登录之后的coolie 那么可以使用cookie进入任何界面

headers = {
    # ':authority': 'weibo.com',
    # ':method': 'GET',
    # ':path': '/u/6426305588',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # cookie携带着你的登录信息 如果有登录之后的coolie 那么可以使用cookie进入任何界面
    'cookie': 'login_sid_t=d8f0999e3ba959bd8cc65775d985918e; cross_origin_proto=SSL; wb_view_log=1536*8641.25; _s_tentry=passport.weibo.com; Apache=1659919627120.6406.1647660269136; SINAGLOBAL=1659919627120.6406.1647660269136; ULV=1647660269149:1:1:1:1659919627120.6406.1647660269136:; ALF=1679196311; SSOLoginState=1647660312; SUB=_2A25PMT1JDeRhGeBK6VQS8CvJwzSIHXVsRymBrDV8PUNbmtANLW7skW9NR8wJ-yz8bFOUXexPyLHFSjb3-IA5JYWt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5jF8slI8N1NVMF7ZTDIUPe5JpX5KzhUgL.FoqXeoq0eh-f1hn2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcShzce05fSKnR; XSRF-TOKEN=lcbetKFN6kRcK3b1xOv0TVjB; WBPSESS=geI_JtjbBZKviSKS9skyYBxOrXBanjJix7OF0pLYRQjYOuMwlfeMOhNb_bomtU54Darzm6qe9vulbPCxLAdj7fV8m89K4biIz5I3TFcFe2cdXd8LiGfbRPFkjruzBMKEO6Ec_Q4WhOQ5uWXyIUeH_A==',
    # referer   判断当前路径是不是由上一个路径进来的  一般情况下是做图片的防盗链
    'referer': 'https://login.sina.com.cn/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应数据
content = response.read().decode('utf-8')

# 将数据保存到本地
with open('weibo2.html', 'w', encoding='utf-8') as fp:
    fp.write(content)