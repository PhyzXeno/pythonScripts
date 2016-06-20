import os

fr = open("4tailNumber.txt","r")
for time in range(1,5):
    time_string = "%d" %time
    fw = open(time_string+".txt","w+")
    for i in range(0,2500):
        fw.write(fr.readline())
    fw.close()
