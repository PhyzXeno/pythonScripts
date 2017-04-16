import os

bina = open("data","rb").read()
binao = open("data2","w")
for i in range(len(bina)):
    binao.write(str(hex(bina[i])).replace('0','\\',1))

binao.close()