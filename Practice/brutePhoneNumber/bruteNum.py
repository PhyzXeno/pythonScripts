import urllib
import http.client as httplib 

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

params = urllib.parse.urlencode({
    'MobileTel':'18811392560',
    'VerifyCodeSerial': '3'
})

conn = httplib.HTTPConnection('www.sjzwhk.com/RetrievePassword.aspx')
conn.request('POST','', params, headers)
response = conn.getresponse()
print(response.status, response.reason)