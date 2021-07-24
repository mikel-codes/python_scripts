from socket import *
from time import ctime

HOST = ''
PORT = 19212
BUFSIZE = 1000
ADDR = (HOST, PORT)
udpServ = socket(AF_INET, SOCK_DGRAM)
udpServ.bind(ADDR)

while True:
    print "UDP Server started at >%s< " % ctime()
    data, addr = udpServ.recvfrom(BUFSIZE)  # anytime its bind to an address(info is recv (port adress and actual info ))
    print "received from to client at" , addr
    udpServ.sendto('[%s] %s' % (ctime(), data), addr)
    if not data:
        break
udpServ.close()
