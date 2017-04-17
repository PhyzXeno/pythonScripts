import threading
import queue

class DoRun(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self._q = q

    def run(self):                  # 这个是override thread的run方法
        while not self._q.empty():
            key = self._q.get()
            print(key)


def main():
    threads = []
    threads_count = 10
    q = queue.Queue()

    for i in range(1,256):
        q.put('106.42.25.'+str(i))

    for i in range(threads_count):
        threads.append(DoRun(q))

    for i in threads:
        i.run()             # 视频中写的是i.start()
    # for i in threads:
    #     i.join()

if __name__ == "__main__":
    main()