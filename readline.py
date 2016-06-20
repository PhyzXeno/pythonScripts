f = open("bingFile.txt","r")
while True:
    line = f.readline()
    if line:
        pass        # do something here
    else:
        break
f.close()