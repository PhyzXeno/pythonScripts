from socket import *
import time

HOST = ""    # 本机作为服务端，地址无需填写
PORT = 2333
BUFSIZE = 1024

ADDR = (HOST, PORT)

tcpServer = socket(AF_INET, SOCK_STREAM)   # stream代表TCP传输
tcpServer.bind(ADDR)      # 绑定到本机的地址和端口上
tcpServer.listen(5)       # 允许的连接数为5

while True:
    print("waiting for connection...")
    tcpClient,addr = tcpServer.accept()   # 如表达式所见，accept返回这两个
    print("..connected from ",addr," ",tcpClient)
    while True:
        data = tcpClient.recv(BUFSIZE)
        if not data:
            break
        tcpClient.send('[%s] %s'%(time.ctime(),data))

tcpClient.close()
tcpServer.close()
