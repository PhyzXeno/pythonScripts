#替换文件中的%20字符为%2B字符（即空格换成加号）
#coding: utf-8 
import os
import re

file_addr = os.getcwd() + '\\' + '123.txt' 
file_i = open(file_addr,'r')        #如果是rb的话，输出是asc码；    
file_i_list = file_i.read()         #这个read出来是一个字符串
strinfo = re.compile('%20')         #正则定位%20
file_i_list_ed = strinfo.sub('%2B',file_i_list)    #把原来的字符串中的%20，替换成%2B

file_o = open(os.getcwd() + '\\' + '456.txt','w')
file_o.write(file_i_list_ed)

file_i.close()
file_o.close()

