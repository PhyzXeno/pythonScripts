import os

base_path = os.getcwd()
file_i = open(base_path + '\\' + '4tailNumber.txt','r')
file_o = open(base_path + '\\' + '1340031.txt','w')

for line in file_i:
    if line:
        file_o.writelines('1340031' + line)