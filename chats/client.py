import socket
import sys
import select
from time import sleep

def send_to():
    uname = raw_input("Enter your chat name >> ")


    print "you can start sending message"
    sys.stdout.write("[%s] >> " %  uname); sys.stdout.flush()

    try:
        while 1:
            socks = [sys.stdin, cli_socks]
            readable,writable, errored = select.select(socks, [], [])
            for sc in readable:
                if sc is cli_socks:
                    data = sc.recv(1024)
                    if data:
                        print ""
                        print "Received" + " > " + data
                        sys.stdout.write("[%s] >> " % uname); sys.stdout.flush()
                    if not data:
                        print "@#### nothin received "
                        print '\nDisconnected from chat server'
                        sys.exit()
                        pass

                else:
                    cli_socks.send(uname)
                    sys.stdout.write ('[%s] >>' % uname ); sys.stdout.flush()
                    msg = sys.stdin.readline(); sys.stdout.flush()
                    cli_socks.send(msg)

    except (SystemExit, KeyboardInterrupt):
        print "You are now offline"

def main():

    p = ' ' * 2 + "Connecting to server"
    print p
    a = '.......'

    for i in range(1):
        sys.stdout.write(p[i])
        sys.stdout.write(a[i])
        sleep(0.2)

    print "\nconnected to the remote server ..... "

    send_to()
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
    #cli_socks.settimeout(2)
    try:
        cli_socks.connect(ADDR)
    except Exception as x:
        x.message = "unable to connect"
        print x.message
        sys.exit()


    sys.exit(main())


