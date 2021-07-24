from SocketServer import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import (ctime, sleep)

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)
class RequestHandler(SRH):    # create object with tcp service handling capabilites
    # this function single handedly handles all handling (give and receive)
    def handler(self):
        print "...connected to >>>", self.client_address
        # wfile ~> write file
        # rfile ~> read file
        self.wfile.write('server >> [%s] %s' % (ctime(), self.rfile.readline()))

if __name__ == '__main__':
    tcps_server = TCP(ADDR, RequestHandler)
    print '>>>>>>>>>  waiting connection <<<<<<<<<<<'
    try:
        tcps_server.serve_forever()
    except (KeyboardInterrupt, Exception), e:
        print " Something happend" , e.message



