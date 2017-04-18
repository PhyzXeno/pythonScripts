import requests
import threading
import time


def spider(url):
    # url = 'http://jandan.net/ooxx'
    headers = {"User-Agent": 'iiiii_spi ver 1.0'}
    r = requests.request("get",url=url,headers=headers)
    print(r.status_code," ",len(r.content))
    # print(str(r.content,encoding='utf8'))
    # time.sleep(1)


urls = []
for i in range(2333,2400):
    url = 'http://jandan.net/ooxx/page-'+str(i)
    urls.append(url)
    # print(url)


threads = []
thread_count = len(urls)

for i in range(thread_count):
    t = threading.Thread(target=spider,args=(urls[i],))
    threads.append(t)

for i in range(thread_count):
    threads[i].start()

for i in range(thread_count):
    threads[i].join()