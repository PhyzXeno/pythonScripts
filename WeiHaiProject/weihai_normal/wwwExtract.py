#!/usr/bin/env python 
# coding=utf-8
import re
#file=open('./weihai1.html','r')
file2=open('./wwwList.txt','a+')
for time in range(1,4):
    time_str="%d" %time
    name='./weihai_nor'+time_str+'.html'
    file=open(name,'r')
    for line in file:
        if "www" in line:
            file2.write(line)
        else:
            pass
file.close()
file2.close()