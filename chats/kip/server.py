import re
import threading
from socket import *
from time import ctime
import select
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
   while True:
       readable, writable, errored = select.select(read_list, [], [], 0)
       for s in readable:
           if s is serv_socks:
               cli_socks, cli_addr = s.accept()
               read_list.append(cli_socks)
               print str(cli_addr) + " status:-online\n "
           else:
               uname = s.recv(1024)  # this represents the first info client will enter (which is his name)
               connections.append((uname, s, cli_socks))
               print "{0} +  is now online as '{1}' ".format((cli_addr), uname)

                #persistent_data(uname)     # check if this name is on admin list
               # uname is the first name it receives after accept as client
               run_event = threading.Event()
               run_event.set()
               try:
                   t = threading.Thread(target=broadcast_user, args=(run_event,))
                   t.start()
               except (SystemExit, KeyboardInterrupt, IOError):
                   print "closing this connection"
                   read_list.remove(s)
                   run_event.clear()
                   t.join()
                   print "connection closed successful"
                   pass
               pass
           pass
       pass
   serv_socks.close()



def broadcast_user(run_event):
         while 1:
            for i in range(len(connections)):
                try:
                    data = connection[i][2].recv(1024)
                    if data:
                        print "{0} said => {1}".format(connections[i][0], data)
                        b_user(connections[i][1], connections[i][0], data)
                    else:
                        print "{0}  {1}".format(connections[i][0], "is now offline")

                        b_user(connections[i][1], connections[i][0], " is now offline ")
                        connections.remove(connections[i])

                except:
                    b_user(connections[i][1], connections[i][0], " is now offline ")
                    continue


        #cli_socks.close()   # if anything happns that makes it leave this loop
    #serv_socks.close()      # exit and close







def b_user(cs_socks, sen_name, msg):
    """send to any person this message apart from the sender"""
    for i in range(len(connections)):
        if connections[i][1] !=  cs_socks:
            try:
                connections[i][1].send(sen_name + " >> " + str(msg))
            except :
                connections[i][1].close()

                if connections[i][0] or connections[i][2] in (connections or read_list):
                    connections.remove(connections[i])
                    read_list.remove(connection[i][1])






def main():
    #funcs = [accept_client]

    print "chat server started on .... ", str(PORT)
    accept_client()


    #for i in range(len(funcs)):
     #   t = threading.Thread(target=funcs[i])
      #  try:
       #     t.start()
       # except Exception as ts:
        #    print ts.message
         #   return



if __name__ == '__main__':
    HOST = ""
    PORT = 9007
    BUFSIZE = 1024
    ADDR = (HOST,PORT)

    connections = []

    serv_socks = socket(AF_INET, SOCK_STREAM)
    serv_socks.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serv_socks.bind(ADDR)
    serv_socks.listen(5)

    read_list = [serv_socks]

    main()
