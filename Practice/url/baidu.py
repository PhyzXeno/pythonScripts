import requests
import sys
import queue
import threading
import bs4
import re
# https://www.baidu.com/s?wd=ichunqiu&pn=10
# wd是所搜索词；pn是链接数，每页有10个链接
# Usage: python baidu.py '关键词'


class BaiduUrl(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._q = queue                                                         
    def run(self):
        if not self._q.empty():
            url = self._q.get_nowait()
            try:
                self.spider(url)
            except Exception as e:
                print(e)
                pass
    def spider(self,url):
        # url = 'https://www.baidu.com/s?wd=java&pn=0'
        header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        }
        r = requests.request("get",url=url,headers=header)
        # print(str(r.content,encoding='utf8'))
        soup = bs4.BeautifulSoup(r.content,'lxml')
        links = soup.find_all(name = 'a',attrs={'data-click':re.compile(('.')),'class':None})    # 定位百度的redirect link
        for link in links:
            # print(links.index(link),link['href'])
            r_link = requests.request("get",url=link['href'])                                    # 取出该link，并访问
            if r_link.status_code == 200:                                                        # 如果访问成功
                # print(r_link.url)
                true_url_list = r_link.url.split('/')                                            # 取出url，并split
                true_url = true_url_list[0]+"//"+true_url_list[2]                                # 拼接出正规的http连接格式
                print(true_url)
                f1 = open('out_url','a+')
                f2 = open('out_para','a+')
                if true_url in f1.readlines():
                    f1.write(true_url+'\n')                                                      # 这个写正规格式
                if r_link.url in f2.readline():
                    f2.write(r_link.url+'\n')                                                    # 这个写实际访问的url
        f1.close()
        f2.close()

def main(keyword):                                                                               # 这块是threa惯用的写法
    q = queue.Queue()
    for i in range(0,200,10):
        q.put("https://www.baidu.com/s?wd="+keyword+"&pn="+str(i))
    threads = []
    thread_count = 10
    for i in range(thread_count):
        threads.append(BaiduUrl(q))
    for i in range(thread_count):
        threads[i].start()
    for i in range(thread_count):
        threads[i].join

if __name__ == '__main__':
    f1 = open('out_url','w')
    f1.close()
    f2 = open('out_para','w')
    f2.close()
    if len(sys.argv) != 2:
        print('Enter %s keyword'%sys.argv[0])
        sys.exit(-1)
    else:
        main(sys.argv[1])
