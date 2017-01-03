#get the binwalk -e command output to a file named output.txt
import os



base_path = os.getcwd()

output = os.popen('binwalk -e ./MT*.bin')

file_o = open(os.getcwd() + '/output.txt' ,'w')
file_o.write(output.read())
file_o.close()

os.system('rm -rf ./_MT*')