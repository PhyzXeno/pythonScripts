import requests
import time
import random

def numRand(a, b):
    return str(random.randint(a, b))

def segIP():
    a = numRand(0, 2)+numRand(0, 5)+numRand(0, 5)
    if a[0]=="0":
        a = a[1:]
        if a[0]=="0":
            a = a[1:]
    return a

def genIP():
    return segIP()+"."+segIP()+"."+segIP()+"."+segIP()


ip = genIP()

header = {
    "Host": "db5.gamersky.com",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Referer": "http://www.gamersky.com/zhuanti/wqj2017/mvt.shtml?wqjpageid=dsjzb",
    "X-Forwarded-For": ip,
    "Connection": "close",
}

url = "http://db5.gamersky.com/Vote/ShowVote.aspx?callback=jQuery18305930459354509029_1514887766825&json=2&userid=0&id=196&vote=3018&_=1514887785475"


# for i in range(10):
#     r = requests.get(url, headers = header)
#     time.sleep(1)
#     print(r.text)

r = requests.get(url, headers = header)
print(r.text[r.text.index("黄旭东"):])