import urllib2
import urllib
 
#定义一个要提交的数据数组(字典)
data = {}
data['username'] = 'zgx030030'
data['password'] = '123456'
 
#定义post的地址
url = 'http://www.test.com/post/'
post_data = urllib.urlencode(data)
 
#提交，发送数据
req = urllib2.urlopen(url, post_data)
 
#获取提交后返回的信息
content = req.read()