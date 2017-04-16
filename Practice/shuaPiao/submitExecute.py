import genIP
import getCookie
import requests
import time
import random

def submitExecute(id):

    cookie = getCookie.getCookie()
    ip = genIP.genIP()
    # print(ip)

    header = {
        "Host": "www.paihang360.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-us",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://www.paihang360.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        # "Referer": "http://www.paihang360.com/mzt/jujiao2017/bidinfo.jsp?record_id=133585",
        "Referer": "http://www.paihang360.com/mzt/jujiao2017/bidinfo.jsp?record_id=" + id,
        "Content-Length": "12",
        "Cookie": "JSESSIONID="+cookie,
        "X-Forwarded-For": ip,
    }

    data = "op=op_submit"

    # url = "http://www.paihang360.com/mzt/jujiao2017/bidinfo.jsp?record_id=133585"
    url = "http://www.paihang360.com/mzt/jujiao2017/bidinfo.jsp?record_id=" + id
    # print(url)

    r = requests.post(url, data, headers=header)
    # print(r.text)

def main():
    id = "130788"
    while 1:
        # sleeptime = random.randrange(50,100,1)
        # time.sleep(sleeptime)
        time.sleep(0.5)
        submitExecute(id)

main()

