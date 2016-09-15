time =1 
base = open("WeiHaiPhoneNumber.txt","r")
registed = open("registedNumber","w+")
for line in base:
    for time in range(1,5):
        time_string = "%d" %time
        tail = open(time_string+".txt","r")
        phoneNumber = line+tail
        req_body = "mobilePhone="+phoneNumber
        print req_body
        req = lib2.Request(req_url, req_headers)
        resp = res.read()
        print resp
        if "1" in resp:
            registed.write(phoneNumber)
    tail.close()
base.close()
registed.close()
