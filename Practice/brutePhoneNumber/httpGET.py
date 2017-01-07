import http.client

url = 'www.sjzwhk.com'
h1 = http.client.HTTPConnection(url) #与特定域名建立HTTP连接
h1.request('GET','/RetrievePassword.aspx') #请求该域名下的directory  HTTPConnection.request(method, url, body=None, headers={}) 
resp = h1.getresponse() #取得反馈
#print(resp.status, resp.reason)
#print(resp.read()) #输出byte型的返回数据

resp_b = resp.read()
