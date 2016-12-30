import os

base_path = os.getcwd()
file_i = open(base_path + '\\' + '1340031.txt', )
for line in file_i:
    dict1={'MobileTel': line,'VerifyCodeSerial': '3'}
    print(dict1['MobileTel'])
    
