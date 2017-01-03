import os

base_path = os.getcwd()

file_name = open(base_path + '/o_name.txt', 'r')
file_number = open(base_path + '/o_number.txt', 'r')  # manually extract the names and numbers....

number = []
name = []

for line in file_number:
    number.append(line)

for line in file_name:
    name.append(line) # get the name and number List

for i in range(len(number) - 1):
    gap = int(number[i + 1]) - int(number[i])
    command_ = 'dd' + ' if=MT-88MW300A_2.0.1.5_0.bin' + ' of=./outfile/' + name[i].strip().replace(' ','_').replace('/','_') + ' skip=' + number[i].strip().replace(' ','_').replace('/','_') + ' count=' + str(gap) + ' bs=1'
    # print(command_)   # check whether the command is right
    os.system(command_)  # do the command
    # os.system('rm /git/pythonScripts/Practice/os.system/outfile/*')

os.system('dd if=MT-88MW300A_2.0.1.5_0.bin of=./outfile/SHA256_hash_constants_little_endian skip=277640 bs=1')  #the last line we do it alone

# notes on dd command:
# 1. the skip number is included
# 2. for example skip=234 count=34:
#    then we get the bytes range: 234~268(234+34) totally 34+1=35 bytes