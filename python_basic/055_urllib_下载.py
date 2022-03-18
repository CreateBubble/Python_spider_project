# _*_ coding: utf-8 _*_
# @file : 055_urllib_下载.py
# @author : sunchuanfu
# @contact:s2271204754@163.com
# @time : 2022/3/17 20:18
# @Version：V 0.1
# @desc :
import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'
#
# urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
# url_img = 'https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=lisa&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=2030561590,1226489879&os=1238677123,3957957874&simid=2030561590,1226489879&pn=35&rn=1&di=7060663421280190465&ln=1296&fr=&fmq=1647519692491_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=0&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fc-ssl.duitang.com%252Fuploads%252Fitem%252F202003%252F27%252F20200327153001_spemx.thumb.1000_0.jpg%26refer%3Dhttp%253A%252F%252Fc-ssl.duitang.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1650111693%26t%3Def54a16623bfc83a0091a9e6d8a64c24&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwzLDYsNCw1LDcsOCwxLDIsOQ%3D%3D'
#
# urllib.request.urlretrieve(url_img, filename='lisa.jpg')
# 下载视频
url_video = 'https://mediago-static.cdn.bcebos.com/haokan/bundle.js?v=1.0.2'

urllib.request.urlretrieve(url_video, filename='../tanhua.mp4')