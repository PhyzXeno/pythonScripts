from socket import *
import time

HOST = "192.168.5.242"    # 连接目标机
PORT = 2333
BUFSIZE = 1024

ADDR = (HOST, PORT)

tcpClient = socket(AF_INET, SOCK_STREAM)
tcpClient.connect(ADDR)

while True:
    data = input('~:')
    if not data:
        break
    tcpClient.send(bytes(data,encoding = "utf8"))
    data = tcpClient.recv(BUFSIZE)
    if not data:
        break
    print(data)

tcpClient.close()