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
}#头部

# base_path = os.getcwd()
# file_i = open(base_path + '\\' + '1340031.txt', )
# for line in file_i:
#     print(line)

params = urllib.parse.urlencode({
    'MobileTel':'18811392561',
    'VerifyCodeSerial': '3'
})#body部分

conn = http.client.HTTPConnection('www.sjzwhk.com')#建立HTTP连接
conn.request('POST','/ashx/Login.ashx?Method=GetRetrieveVerifyCode', params, headers)#发送POST请求
response = conn.getresponse()#取得response对象
#print(response.status, response.reason)
#print(response.read())

resp_bytes = response.read()#读取response对象，read出来的是byte类型数据（即一个一个输出是asc码）
resp_str = str(resp_bytes, encoding='utf-8')#byte转换为str型数据
print(resp_str)#显示一下str