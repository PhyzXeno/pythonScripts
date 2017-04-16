import random

def numRand(a, b):
    return str(random.randint(a, b))

def segIP():
    a = numRand(0, 2)+numRand(0, 5)+numRand(0, 5)
    if a[0]=="0":
        a = a[1:]
        if a[0]=="0":
            a = a[1:]
    return a

def genIP():
    return segIP()+"."+segIP()+"."+segIP()+"."+segIP()

# print(genIP())

