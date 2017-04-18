import requests
import bs4
import re

url = 'https://www.baidu.com/s?wd=java&pn=0'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
r = requests.request("get",url=url,headers=header)
# print(str(r.content,encoding='utf8'))

soup = bs4.BeautifulSoup(r.content,'lxml')

links = soup.find_all(name = 'a',attrs={'data-click':re.compile(('.')),'class':None})

for link in links:
    # print(links.index(link),link['href'])
    r_link = requests.request("get",url=link['href'])
    if r_link.status_code == 200:
        print(r_link.url)