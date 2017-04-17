# http://www.heibanke.com/lesson/crawler_ex02/
import requests
import re

pattern = re.compile(r'<h3>.*?</h3>')
def findStr(text):
    search = pattern.search(text).group()
    return search

header = {
    "Host": "www.heibanke.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://www.heibanke.com/lesson/crawler_ex02/",
    "Cookie": "Hm_lvt_74e694103cf02b31b28db0a346da0b6b=1492409956; Hm_lpvt_74e694103cf02b31b28db0a346da0b6b=1492412635; csrftoken=OYVz25NrWKCkL5mevbOSdIhf1ters16h; sessionid=vgcnti0t1mr6rnlbk6akdhbyal5dau8h",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "80",

}

url = "http://www.heibanke.com/lesson/crawler_ex02/"

body0 = "csrfmiddlewaretoken=OYVz25NrWKCkL5mevbOSdIhf1ters16h&username=firefox&password="
for i in range(0,31):
    body = body0 + str(i)
    r = requests.request("post", url=url, headers=header, data=body)
    try:
        print(findStr(r.text))
    except:
        print(body)
        print(r.text)
        
    


