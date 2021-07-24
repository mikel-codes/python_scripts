from socket import *
import select
import sys
#import pdb


def persistent_data(username):
    try:
        f = open("/root/Desktop/x_client.txt")
        for i in f.readlines():
            if i != username:
                print "invalid user login"
                print "contact system administrator"
                break
            print "welcome to chatroom .... ", username
    except Exception as fe:
        print fe.message
        return


def accept_client():
   # pdb.set_trace()
   try:
       while True:
           readable, writable, errored = select.select(read_list, [], [], 0)
           for s in readable:
               if s is serv_socks:
                   cli_socks, cli_addr = serv_socks.accept()
                   read_list.append(cli_socks)
                   print str(cli_addr) + " status:-online "
               else:

                   uname = s.recv(1024)
                   data = s.recv(1024)

                   try:
                       if [b[1] for b in connections].index(s):
                           #b_user(serv_socks, s, uname, uname)
                           broadcast_user(data, b[0], s)
                   except:
                       connections.append((uname, s))
                       a = "{0} is now online as {1} ".format(str(s.getpeername()), uname)
                       print a
                       b_user(serv_socks, s, uname , a)
                   #finally:
                    #   accept_client
                   pass
               pass


   except (SystemExit, KeyboardInterrupt, IOError):
           print ""
           print "closing this connection"
           del connections[:]
           del read_list[:]
           print "connection closed successful"
           #sys.exit(broadcast_user())

   serv_socks.close()


def broadcast_user(data, username, xlc):
    #readable, writable, errored = select.select(read_list, [], [], 0)
    #data = xlc.recv(1024)
    if data:
        print "{0} said => {1}".format(username, data)
        b_user(serv_socks, xlc , username, data)

    else:
        print "{0}  {1}".format(username,  "is now offline")
        b_user(serv_socks, xlc, username, "is now offline ")

def b_user(sv_socks, cs_socks, sen_name, msg):
    """send to any person this message apart from the sender"""
    for socks in  read_list:
        if socks != serv_socks or socks ==  cs_socks:
            try:
                socks.send(sen_name + " >> " + str(msg))
            except :
                socks.close()

                if socks in read_list:
                    read_list.remove(socks)



def main():
    print "chat server started on .... ", str(PORT)
    accept_client()


if __name__ == '__main__':
    HOST = ""
    PORT = 9007
    #BUFSIZE = 1024
    ADDR = (HOST,PORT)

    serv_socks = socket(AF_INET, SOCK_STREAM)
    serv_socks.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serv_socks.bind(ADDR)
    serv_socks.listen(5)

    read_list = [serv_socks]

    connections = []
    sys.exit(main())
