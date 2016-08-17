import os
import urllib2

base_address='http://tongzhuo.zhuma.mobi/tz/controller/data/1/notes?cuser_id='
file=open('C:/Users/Lin/Desktop/hahah.txt','w+')
for number in range(3528850,3528860+1):
    number_str='%d'%number
    file.write(urllib2.urlopen(base_address+number_str).read())

file.close()
