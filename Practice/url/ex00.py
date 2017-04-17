import requests
import re

pattern = re.compile(r'<h3>.*?\d{5}')
def findNum(text):
    search = pattern.search(text)
    temp = search.group()[-5:]
    return temp


url = "http://www.heibanke.com/lesson/crawler_ex00/"

a = ''
for i in range(100):
    try:
        r = requests.request("get",url = url+a)
        a = findNum(r.text)
        print(a)
    except:
        print(r.text)
