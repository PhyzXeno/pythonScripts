import requests
import re

url = 'http://bbs.ichunqiu.com'

r = requests.request("get", url=url)

bbs_news = re.findall('class="ui_colorG" style="color: #555555;">(.*?)</a></h3>',str(r.content, encoding = "utf8"))

for i in bbs_news:
    print(i)

# print(r.status_code)
# print(str(r.content, encoding = "utf8"))