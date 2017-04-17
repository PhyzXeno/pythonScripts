# http://www.heibanke.com/lesson/crawler_ex01/
import requests
import re

pattern = re.compile(r'<h3>.*?</h3>')
def findStr(text):
    search = pattern.search(text).group()
    print(search)


header = {
    "Host" : "www.heibanke.com",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": 'gzip, deflate' ,
    "Referer" : "http://www.heibanke.com/lesson/crawler_ex01/",
    "Cookie" : "Hm_lvt_74e694103cf02b31b28db0a346da0b6b=1492409956; Hm_lpvt_74e694103cf02b31b28db0a346da0b6b=1492411045; csrftoken=uzBMHs14JHbBjNI2J6Ai5I8ZFBvl7FBd",
    "Connection" : "keep-alive",
    "Upgrade-Insecure-Requests" : "1",
    "Content-Type": r'application/x-www-form-urlencoded',
    "Content-Length" : "80",
}

body0 = "csrfmiddlewaretoken=uzBMHs14JHbBjNI2J6Ai5I8ZFBvl7FBd&username=firefox&password="

url = "http://www.heibanke.com/lesson/crawler_ex01/"

for i in range(0,31):
    body = body0 + str(i)
    print(body)
    r = requests.request("post", url=url, headers=header, data=body)
    findStr(r.text)
