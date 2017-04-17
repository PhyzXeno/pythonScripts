import re

valid = re.compile(r"^[a2-9tjqk]{5}$")
print(valid.match("akt5q").group())