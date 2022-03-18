# -*- coding: utf-8 -*-
# @File : 060_post百度翻译之详细翻译.py
# @Author  : Bubble
# @Time    : 2022/3/18 13:40
# @Function:

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '136',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BIDUPSID=6D89A5C58BF3CAFA4585F250BA5E943A; PSTM=1646718302; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; APPGUIDE_10_0_2=1; __yjs_duid=1_4b33e4500b92bbdfe78e3e46b6f088cb1646815991539; BDUSS=2I0NXpENTM1fjZoTm5YU0FmNy13NU5ZelVNQktWWjFOdnd5NkdnTkZncGR-RTlpSVFBQUFBJCQAAAAAAAAAAAEAAAAvB-BLU72jyqW0q8bmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF1vKGJdbyhib; BDUSS_BFESS=2I0NXpENTM1fjZoTm5YU0FmNy13NU5ZelVNQktWWjFOdnd5NkdnTkZncGR-RTlpSVFBQUFBJCQAAAAAAAAAAAEAAAAvB-BLU72jyqW0q8bmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF1vKGJdbyhib; BAIDUID=4010DE4E33A2E3727739520D83EFBC8F:FG=1; BAIDUID_BFESS=B73D4821C305BDEF8D4DB65DC214E971:FG=1; RT="z=1&dm=baidu.com&si=3q33v53krhw&ss=l0w02uc5&sl=2&tt=2dp&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&cl=7yu&ld=375&ul=8z07&hd=8z0s"; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; H_PS_PSSID=35836_35105_31254_36087_34584_36073_36065_36109_35319_26350_36115_35877_22159_36061; BA_HECTOR=042h2l0k858gag21le1h38c5s0q; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1646815991,1647579894,1647588068; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1647588131; ab_sr=1.0.1_NDc3MGQ0M2JhNmE5M2FmY2E0NzA2NmMwYzlmNDZhYTMyZDczN2I4ZDlhYjIwZDY4MDE2MTEyN2YwOWRkYWM0NjNkNWY0OGY0ODk3NGFmYjRkZTk5MTkwZjI4YjU3NmIyZDRlNTU1NWVhOTMzYTE3YzRlZmU1NGU1NzgwOTliMzgxMWJkOTQ1NjllMTgwMTEyNGJjN2YzYTQ1YTA2NGEyYmM0MjI2ZTNkNDk5ODgwMzQ4ODk1OTEwOWQyNDY3MDhm',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'a16b1c48300d1708343d2d0947627237',
    'domain': 'common'
}

# post请求的参数，必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象定制的参数中
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')
obj = json.loads(content)
print(obj)