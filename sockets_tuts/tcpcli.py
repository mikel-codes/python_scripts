from socket import *

HOST = "127.0.0.1"
PORT = 22831
BUFSIZE = 1000
ADDR = (HOST, PORT)


tcpCliSocks = socket(AF_INET, SOCK_STREAM)
tcpCliSocks.connect(ADDR)

while True:
    info = raw_input("client >>")
    if not info:
        break
    tcpCliSocks.send(info)
    info = tcpCliSocks.recv(BUFSIZE)
    if not info:
        break
    print info

tcpCliSocks.close()
