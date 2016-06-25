#!/usr/bin/env python
# coding=utf-8
import re

file=open('/root/Desktop/yes.html','r')
buf=file.readlines()
stg=str(buf)
file2=open('/root/Desktop/list','w+')

r=r'"http://download.*?"'
#r=r'\w{3}'
#r=r"\w{1,3}?"
#r=r'href=.*?\s+?'
xxmap=re.compile(r)
map=xxmap.findall(stg)
for addr in map:
    file2.write(addr)
    file2.write('\n')
file.close()
file2.close()

