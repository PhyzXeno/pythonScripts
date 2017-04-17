import threading
import time

def fun1(key):
    print("hello world: ",key,time.ctime())
    print("\n")

def main():
    threads = []
    keys = ["1 ","2 ","3 "]

    threads_count = len(keys)

    for  i in range(threads_count):
        t = threading.Thread(target=fun1,args=(keys[i],))
        threads.append(t)

    for i in range(threads_count):
        threads[i].start()

    for i in range(threads_count):
        threads[i].join()

if __name__ == "__main__":
    main()