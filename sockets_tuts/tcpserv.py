from socket import *
from time import ctime

HOST = ""
PORT = 22831
BUFSIZE = 1000
ADDR = (HOST, PORT)

tcpServer = socket(AF_INET, SOCK_STREAM)
tcpServer.bind(ADDR)
tcpServer.listen(3)

while True:
    print "Server started ...."
    print ">>> connection awaited >>>"
    tcpCliSocks, addr = tcpServer.accept()
    print "<<<<<<<< connected to " , addr
    while True:
        infomat = tcpCliSocks.recv(BUFSIZE)   # receive connection from back-end client
        if not infomat:
            break  # if it recieves nothing from client close connection
        tcpCliSocks.send("server >> [%s] -> received :%s " % (ctime(), infomat))   #else snd d client his info with a date stamped
        pass
    tcpCliSocks.close()
    pass
tcpServer.close()
