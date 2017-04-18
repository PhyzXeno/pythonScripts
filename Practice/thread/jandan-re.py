import requests
import re
from bs4 import BeautifulSoup

url = "http://jandan.net/pic/page-645"
headers = {'User-Agent':"Firefox 1.0"}
r =requests.request("get",url = url,headers=headers)

soup = BeautifulSoup(r.content,'lxml')

imgs = soup.find_all(name='img',attrs={})

for img in imgs:
    print(img['src'])