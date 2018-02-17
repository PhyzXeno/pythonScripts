import subprocess

cmd = ["curl", "ip4.me"]
subprocess.Popen(cmd)
f = open("output", "w")
f.write(output)

