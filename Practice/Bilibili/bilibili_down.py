import requests
import re
import ast
import sys
import os

id = sys.argv[1]
print("the id is" + str(id))
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Cookie" : "sid=59bo484f; buvid3=A13536B3-4171-49FA-8A13-35A1A729C68A14072infoc; LIVE_BUVID=AUTO6715179853023347; fts=1517985341; finger=dd823f11; pgv_pvi=1014652928; rpdid=kmoxkplkoldosomlqskww"
    }  # need cookie to work with url (caught from browser)
url = "http://api.bilibili.com//playurl?aid=" + id + "&page=1&platform=html5&quality=1&vtype=mp4&type=jsonp&callback=fn&token=d3bd9275f0f2cda07f2406740db06c5d&callback=mduijsonp_1518883361692_9"  # the bilibili api to reveal the real url
r = requests.get(url,headers = headers)
the_str = r.text.encode('utf-8').decode('unicode_escape')
the_str = the_str.replace("\\", "")  # replace "\"

pattern = '\(.*\)'  # extract the str in between the ()
match = re.compile(pattern).search(the_str).group()  # the standard way to use re
the_dict = ast.literal_eval(match[1:-1]) # get the str and convert it into dict
the_url = the_dict["durl"][0]["url"] # get the index of durl and then the url
print(the_url)  # print the url
print("start downloading to /home/lin/mydown")
cmd = "aria2c -d /home/lin/mydown -s 5 " + "\"" + the_url + "\""
os.system(cmd)
