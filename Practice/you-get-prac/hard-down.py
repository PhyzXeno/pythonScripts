import os

def down(url, outdir):
    cmd = "python  C:/Users/Lin/Git/you-get/you-get " + " -o " + outdir+ " " + url
    print(cmd)
    a = os.system(cmd)
    print(a)
    #print(a.stdout.read())

def main():
    outdir = "G:/Courses/HardwareSister"
    url = [
        "www.bilibili.com/video/av7624536",
        "www.bilibili.com/video/av7731555",
        "www.bilibili.com/video/av7511232",
        "www.bilibili.com/video/av8430358",
        "www.bilibili.com/video/av7657552",
        "www.bilibili.com/video/av7990003",
        "www.bilibili.com/video/av9005330",
        "www.bilibili.com/video/av8889023",
        "www.bilibili.com/video/av9162261",
        "www.bilibili.com/video/av7222011",
        "www.bilibili.com/video/av8460893",
        "www.bilibili.com/video/av7329348",
        "www.bilibili.com/video/av8527069",
        "www.bilibili.com/video/av7431414",
        "www.bilibili.com/video/av7230090",
        "www.bilibili.com/video/av7421294",
        "www.bilibili.com/video/av9022975",
        "www.bilibili.com/video/av8803876",
        "www.bilibili.com/video/av8117587",
        "www.bilibili.com/video/av7315950",
        "www.bilibili.com/video/av7335052",
        "www.bilibili.com/video/av7494052",
        "www.bilibili.com/video/av7242940",
        "www.bilibili.com/video/av8668454",
        "www.bilibili.com/video/av8078244",
        "www.bilibili.com/video/av7305273",
        "www.bilibili.com/video/av7406509",
        "www.bilibili.com/video/av7222011",
        "www.bilibili.com/video/av7551298",
        "www.bilibili.com/video/av8631862",
        "www.bilibili.com/video/av7391897",
        "www.bilibili.com/video/av7068192",
        "www.bilibili.com/video/av6917513",
        "www.bilibili.com/video/av7094105",
        "www.bilibili.com/video/av6999449",
        "www.bilibili.com/video/av7219459",
        "www.bilibili.com/video/av6949068",
        "www.bilibili.com/video/av7052358",
        "www.bilibili.com/video/av7014829",
        "www.bilibili.com/video/av7106012", 
        "www.bilibili.com/video/av7156568",
        ] 
    url = list(set(url))
    for i in range(0,len(url)):
        down(url[i], outdir)
main()