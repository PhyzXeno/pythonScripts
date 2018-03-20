regex = r"^(a+)+$"
maketeststring = lambda n: "a" * n + "!"
maxiter = 50
maxtime = 2

import re
import time
import sys

def main():
    print 
    print "Python Regular Expression DoS demo"
    print "from http://www.computerbytesman.com/redos"
    print 
    print "Platform         %s %s" % (sys.platform, sys.version)
    print "Regular expression   %s" % (regex)
    print "Typical test string:     %s" % (maketeststring(10))
    print "Max. iterations:     %d" % (maxiter)
    print "Max. match time:     %d sec%s" % (maxtime, "s" if maxtime != 1 else "")
    print 
    cregex = re.compile(regex)
    for i in xrange(1,maxiter):
        time = runtest(cregex, i)
        if time > maxtime:
            break
    return

def runtest(regex, n):
    teststr = maketeststring(n)
    starttime = time.clock()
    match = regex.match(teststr)
    elapsetime = int((time.clock()-starttime) * 1000)
    count = 0 
    if match != None:
        count = match.end() - match.start()
    print "For n=%d, match time=%d mesc%s, match count=%s" % (n, elapsetime, "s" if elapsetime == 1 else "", count)
    return float(elapsetime) / 1000


if __name__ == "__main__":
    main()