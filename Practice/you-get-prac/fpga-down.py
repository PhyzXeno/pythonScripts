# import subprocess
# import sys

# def down(url, outdir):
#     cmd = "python  C:/Users/Lin/Git/you-get/you-get " + " -o " + outdir+ " " + url
#     print(cmd)
#     a = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
#     for line in iter(a.stdout.readline, b''):
#         print(line.decode("utf-8"))
#     a.stdout.close()
#     a.wait()

# def main():
#     outdir = "G:/Courses/FPGA"
#     url=[   "http://www.bilibili.com/video/av5830795/",   
#             "http://www.bilibili.com/video/av5830488/",
#             "http://www.bilibili.com/video/av5830121/",
#             "http://www.bilibili.com/video/av5828493/",
#             "http://www.bilibili.com/video/av5826918/",
#             "http://www.bilibili.com/video/av5825223/",
#          ] 
#     for i in range(0,len(url)):
#         down(url[i], outdir)
# main()



import os

def down(url, outdir):
    cmd = "python  C:/Users/Lin/Git/you-get/you-get " + " -o " + outdir+ " " + url
    print(cmd)
    a = os.system(cmd)
    print(a)
    #print(a.stdout.read())

def main():
    outdir = "G:/Courses/FPGA"
    url=[   "http://www.bilibili.com/video/av5830795/",   
            "http://www.bilibili.com/video/av5830488/",
            "http://www.bilibili.com/video/av5830121/",
            "http://www.bilibili.com/video/av5828493/",
            "http://www.bilibili.com/video/av5826918/",
            "http://www.bilibili.com/video/av5825223/",
         ] 
    for i in range(0,len(url)):
        down(url[i], outdir)
main()
