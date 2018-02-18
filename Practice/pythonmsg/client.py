import socket

f = open('/home/lin/temp', 'rb')

s = socket.socket()
s.connect(('45.76.106.207', 12345))
s.sendall(f.read())
s.close
