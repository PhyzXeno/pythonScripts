import requests
import threading
import time
import queue

class JanSpider(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self._q = q

    def run(self):
        while not self._q.empty():
            page_url = self._q.get_nowait()
            # print(page_url)
            self.spider(page_url)
    
    def spider(self,url):
        # url = 'http://jandan.net/ooxx'
        headers = {"User-Agent": 'iiiii_spi ver 1.0'}
        r = requests.request("get",url=url,headers=headers)
        print(r.status_code," ",len(r.content))
        # print(str(r.content,encoding='utf8'))
        # time.sleep(1)



def main():
    q = queue.Queue()
    for i in range(2333,2350):
        q.put('http://jandan.net/ooxx/page-'+str(i))

    threads = []
    thread_count = 10

    for i in range(thread_count):
        threads.append(JanSpider(q))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()