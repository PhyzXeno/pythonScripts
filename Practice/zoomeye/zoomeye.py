import requests
import bs4
import re

url = 'https://www.zoomeye.org/search?t=host&q=tomcat'
header = {
    'Host': 'www.zoomeye.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/css,*/*;q=0.1',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https:///www.zoomeye.org/search?q=tomcat&t=host',
    'Cookie': '__jsluid=513961e0b739412c14bfc6ea93d7e4e3; __jsl_clearance=1492522612.643|0|s%2FpnmkzaczWLb7ioW74g8Ri16YI%3D; Hm_lvt_e58da53564b1ec3fb2539178e6db042e=1492522609; Hm_lpvt_e58da53564b1ec3fb2539178e6db042e=1492522618',
    'Connection': 'keep-alive',
    'If-Modified-Since': 'Mon, 01 Aug 2016 09:31:35 GMT',
    'If-None-Match': 'W/"579f16f7-7242"',
    'Cache-Control': 'max-age=0',
}

def spider(url):
    r = requests.request('get',url=url,headers=header)

    # print(r.status_code)
    # print(r.content)

    soup = bs4.BeautifulSoup(r.content,'lxml')
    ips = soup.find_all(name='a',attrs={'class':'ip'})
    ports = soup.find_all(name='i',attrs={'class':None})
    # for ip in ips:
    #     print(ip.string)
    # for port in ports:
    #     print(port.string.replace('\n',' ').replace(' ',' ').lstrip())   # lstrip就是左对齐，rstrip就是右对齐，strip就是去各种空白

    for ip,port in zip(ips,ports):
        print(ip.string,port.string.replace('\n',' ').replace(' ',' ').lstrip())

def main():
    for i in range(1,11):
        url = 'https://www.zoomeye.org/search?t=host&q=tomcat&p='+str(i)
        spider(url)

if __name__ == "__main__":
    main()