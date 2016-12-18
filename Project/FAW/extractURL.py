import os

# for file_name in os.listdir(os.getcwd()):
#     print(file_name)

file_list = os.listdir(os.getcwd())

file_out = open(os.getcwd() + '/' + '123.txt','a+')

for i in range(0,len(file_list)):
    if 'html' in file_list[i]:
        #print(file_list[i])
        file_in = open(os.getcwd() + '/' + file_list[i], 'r')
        for line in file_in:
            if 'faw' in line:
                file_out.write(line)

file_in.close()
file_out.close()