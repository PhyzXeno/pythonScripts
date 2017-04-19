import requests
import json


def auth():
    url_login = "https://api.zoomeye.org/user/login"
    data = {
        "username": "630172407@qq.com",
        "password": "z00meye!@#",
    }
    data = json.dumps(data)    # body部分需要是json格式
    r = requests.request("post",url=url_login,data=data)
    # print(r.content)
    # print(json.loads(r.content)['access_token'])
    return(json.loads(r.content)['access_token'])

def main():
    url = 'https://api.zoomeye.org/host/search?query=zabbix'
    headers = {
        'Authorization': 'JWT '+auth(),
    }
    r = requests.request('get',url=url,headers=headers)
    # print(r.status_code,r.content)
    content = json.loads(r.content)['matches']
    for data in content:
        print(data['ip'])

main()