from socket import *

HOST = '127.0.0.1'
PORT = 19212
BUFSIZE = 1000
ADDR = (HOST, PORT)
udpCli = socket(AF_INET, SOCK_DGRAM)

while True:

    data = raw_input('client >')
    if not data:
        break;
    udpCli.sendto(data, ADDR)
    data, addr = udpCli.recvfrom(BUFSIZE)
    if not data:
        print "No input \n closing this client "
    print data
udpCli.close()
