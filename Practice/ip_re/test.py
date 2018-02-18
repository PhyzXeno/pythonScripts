import os
import re

ip = "ip4.me"
cmd = "curl -qs " + ip
output = os.popen(cmd).read()

pattern = "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
r = re.compile(pattern).search(output).group()
print(r)
