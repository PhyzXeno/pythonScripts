import requests

id = "19618640"
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Cookie" : "sid=59bo484f; buvid3=A13536B3-4171-49FA-8A13-35A1A729C68A14072infoc; LIVE_BUVID=AUTO6715179853023347; fts=1517985341; finger=dd823f11; pgv_pvi=1014652928; rpdid=kmoxkplkoldosomlqskww"
    }
url = "http://api.bilibili.com//playurl?aid=19618640&page=1&platform=html5&quality=1&vtype=mp4&type=jsonp&callback=fn&token=d3bd9275f0f2cda07f2406740db06c5d&callback=mduijsonp_1518883361692_9"
r = requests.get(url,headers = headers)
print(r.text.encode('utf-8').decode('unicode_escape'))
# print(r.cookies)
