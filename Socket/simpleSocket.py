import socket

ipAddr = '61.135.169.125'   #baidu ip

req1 = b"GET / HTTP/1.0\r\n\r\n"  #b for bytes type

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ipAddr, 80))
client_socket.send(req1)

print(client_socket.recv(1024))
print("hello world\n")