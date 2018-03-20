import re

file = open('view-source_www.sinomach.com.cn.html','r',encoding='utf-8')    # 以utf-8编码，只读模式打开一个html源代码
print(type(file))

abc = re.findall(r'<a href=".*?"', file.read())                             # 使用findall函数来进行正则匹配
for i in range(len(abc)):
    print(abc[i])                                                           # 结果一个个打印出来

