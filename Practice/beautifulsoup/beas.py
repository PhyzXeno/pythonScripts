from bs4 import BeautifulSoup
import re
import requests

file = open("ichuiqiu_bbs.html", 'rb')
html_doc = file.read()

soup = BeautifulSoup(html_doc, 'lxml')

# print(soup.title)
# print(soup.title.string)

for i in soup.find_all(name='a', attrs={'class':re.compile('ui_colorG')}):
    print(i.string)