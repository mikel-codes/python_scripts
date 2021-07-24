import socket
import sys
import select

def send():

    uname = raw_input("Enter your chat name >> ")
    cli_socks.send(uname)

    while True:
         read_cli_list = [cli_socks]
         readable, writable, errored = select.select(read_cli_list, [],[])
         for s in readable:
             if s is cli_socks:
                data = raw_input(' %s >> ' % uname)
                cli_socks.send(data)
             else:
                 receive()




def receive():
    try:
        data = cli_socks.recv(1024)
        if not data:
            print "@#### nothin received "
            print '\nDisconnected from chat server'
            sys.exit()

        else:
             # it only receives data as named by server
            print ('\n' + "Received" + " > " + str(data))
    except:
        sys.exit()




def main():

    send()
    #for i in range(len(funcs)):
     #   t = threading.Thread(target=funcs[i])
      #  try:
       #     t.start()
       # except Exception as ts:
        #    print ts.message
         #   return

if __name__ == '__main__':

    HOST = 'localhost'
    PORT = 9007
    ADDR = (HOST,PORT)


    cli_socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_socks.settimeout(3)
    try:
        cli_socks.connect(ADDR)
    except Exception as x:
        x.message = "unable to connect"
        print x.message
        sys.exit()

    print "connected to the remote server ..... "

    sys.exit(main())


