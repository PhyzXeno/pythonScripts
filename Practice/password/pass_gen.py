import exrex
import sys

# words which cannot probably be used in password
web_white = ['com','cn','gov','edu','org','www'] 

def host_parse(host):
    # analyze host to get the format we want
    if '://' in host:
        host = host.split('://')[1].replace('/','')
    if '/' in host:
        host = host.replace('/','')
    return(host)

def dic_create(hosted):
    # get the words from an url(here we call it host) to create dict
    # we want to write the exrex generating rules into a config file
    web_dicts = hosted.split('.')
    f_pass = open('password','r')
    f_rule = open('config','r')
    rule_lines = f_rule.readlines()
    f_pass_lines = f_pass.readlines()
    # print(f_rule.readlines()[2])
    for rule in rule_lines:
        if '#' in rule[0]:
            # print(rule)
            continue
        else:
            print(rule)
            for web_dict in web_dicts:
                if web_dict not in web_white:
                    for passw in f_pass_lines:
                        # combine the passwords with the parsed hosts
                        dicts = list(exrex.generate(rule.format(web_dict=web_dict, passw=passw.strip())))
                        for dic in dicts:
                            print(dic)

dic_create(host_parse('demo.webdic.com'))    
# if __name__ == "__main__":
#     if len(sys.argv) == 2:
#         dic_create(host_parse(sys.argv[1]))
#         sys.exit(0)
#     else:
#         print 'Usage:%s www.demo.com'%sys.argv
#         sys.exit(-1)
        

