import os 

os.chdir('/media/root/2CD67EE9D67EB3261/jack')
fileNameList = os.listdir(os.getcwd())

addr_list = []
for i in range(1,len(fileNameList)):
    #print(fileNameList[i][:])
    if 'Frag' in fileNameList[i]:
        b_index = fileNameList[i].index('Frag')
        addr_list.append(fileNameList[i][(b_index - 26):(b_index - 15)])

url_string = list(set(addr_list))

file_o = open(os.getcwd()+'/'+'url_string.txt','w+')
for i in range(1,len(url_string)):
    file_o.write('youtube-dl -i --proxy socks5://127.0.0.1:9001 https://www.youtube.com/watch?v=')
    file_o.write(url_string[i])
    file_o.write('\n')

file_o.close()
        
#print(len(fileNameList))