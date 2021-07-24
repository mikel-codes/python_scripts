from socket import *
import sys

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1000
ADDR = (HOST, PORT)

while True:
    try:
        tcpCliSocks = socket(AF_INET, SOCK_STREAM)
        tcpCliSocks.connect(ADDR)
        data = raw_input('client >> ')
        if not data:
            break

        tcpCliSocks.send('%s\r\n' % data)
        data = tcpCliSocks.recv(BUFSIZE)
        if not data:
            break
        print data.strip()
        tcpCliSocks.close()
    except error, e:
        print "socket errors occured [%s]:%s" % (e, e.errno)
        print sys.exc_info
        sys.exit(1)
