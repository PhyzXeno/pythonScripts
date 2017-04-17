import re

# 显示一个对象的类型
def printType(a):
    print(type(a))                                                                 

# 打印出正则匹配结果
def printReg(pattern, string):
    match = re.compile(pattern).search(string).group()
    print(match)

# 正则表达式
pattern = '<a href=".*?"'

# 打开文件
file = open('view-source_www.sinomach.com.cn.html','r',encoding='utf-8')

# 按行读取成list
lists = file.readlines()

# 输出匹配结果
for i in range(len(lists)):
    try:
        printReg(pattern, lists[i])
    except:
        pass

#关闭文件
file.close()

