import http.client

url = 'www.sjzwhk.com'
h1 = http.client.HTTPConnection(url)
h1.request('GET','/')
resp = h1.getresponse()
#print(resp.status, resp.reason)
print(resp.read())