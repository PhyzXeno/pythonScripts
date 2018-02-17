import requests

id = "19618640"
url = "http://api.bilibili.com/view?type=jsonp&appkey=8e9fc618fbd41e28&id=" + id + "&page=1&callback=fn"
url2 = "http://api.bilibili.com//playurl?aid=" + id + "&page=${ value }&platform=html5&quality=1&vtype=mp4&type=jsonp&callback=fn&token=d3bd9275f0f2cda07f2406740db06c5d"
r = requests.get(url2)
print(r.text.encode("utf-8").decode("unicode_escape"))