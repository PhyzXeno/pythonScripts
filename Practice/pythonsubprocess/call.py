import subprocess

url = 'ip4.me'
cmd = ['df', '-h']
cmd2 = ['curl', url]
subprocess.call(cmd2)
