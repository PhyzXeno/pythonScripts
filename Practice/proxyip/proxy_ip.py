import requests
import bs4
import re

def proxy_spider():
    url = 'http://www.xicidaili.com/nn'
    header = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            }
    r = requests.request('get',url=url,headers=header)

    soup = bs4.BeautifulSoup(r.content,'lxml')
    ips = soup.find_all(name = 'tr',attrs={'class':re.compile('|(^odd)')})

    # for ip in ips:
    #     print(ip['td'])
    # print(str(r.content,encoding='utf8'))

    for ip in ips:
        proxy = {}         # 一个代理一个字典
        ip_soups = bs4.BeautifulSoup(str(ip),'lxml')
        ip_soup = ip_soups.find_all(name = 'td')
        the_ip = ip_soup[1].string
        the_port = ip_soup[2].string
        the_protocol = ip_soup[5].string.lower()
        proxy[the_protocol] = '%s:%s'%(the_ip,the_port)
        # print(proxy)
        # print(str(proxy.values())[:])
        proxy_check(proxy)

        
def proxy_check(proxy):
    #  print(proxy)
     try:
        r = requests.request('get',url='http://1212.ip138.com/ic.asp',proxies=proxy,timeout=6)    # 如果proxies不好用的话，就会使用本机的ip
        # print(r.text)
        ip_content = re.findall(r'\[(.*?)\]',r.text)[0]         # 提取出返回内容中的ip地址，即ip138识别的地址
        if ip_content in str(proxy.values()):                   # 判定返回值和proxy字典相符的，说明是可用的代理
            print(proxy)
     except Exception as e:
        # print(e)
        pass

def proxy_check0():                   # 这个函数仅用于验证代理服务器的可用性
    proxy = {'http':'119.5.0.110:808'}                     # 此处写上代理服务器的字典
    r = requests.request('get',url='http://1212.ip138.com/ic.asp',proxies=proxy)   # 在request里面写上proxies参数即可！
    print(r.text)                        # 显示本机的ip地址

proxy_spider()