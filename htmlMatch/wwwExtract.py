#!/usr/bin/env python 
# coding=utf-8
import re

file=open('./weihai.html','r')
buf=file.readlines()
stg=str(buf)
file2=open('./wwwList.txt','w+')

r=r'"www.*$"'
xxmap=re.compile(r)
map=xxmap.findall(stg)
for addr in map:
    file2.write(addr)
    file2.write('\n')
file.close()
file2.close()