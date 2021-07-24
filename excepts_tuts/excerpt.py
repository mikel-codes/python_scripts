#! /usr/bin/python

import os, socket, tempfile, errno

#create custom Exception Types derived from standard errors

class FileError(IOError):
    pass

class NetworkError(IOError):
    pass



def updArgs(args, newargs=None):
    ''' This becomes a method to be adopted by custom exception class'''
    if isinstance(args, IOError):
        myargs = []     #create an empty array
        myargs.extend([arg for arg in args ])   # expand this array with an exclusive list of IOError objects
    else:
        myargs = list(args)   # whatever is not an object type of IOError myargs should be returned as a list

    if newargs:
        myargs.append(newargs)      # if there are exceptional args to this method
                                    # add it towards the end of this list

    return tuple(myargs)   #overall make this returned list inelastic


def fileArgs(file, mode, args):
    # we check if we find a permission denied on a file and whether the os
    # support file permissions checking

    if args[0]  == errno.EACCES and 'access' in dir(os):
        # lets first create an empty string
         perms = ''
         # build a permission dictionary with strings tied to the os_type code
         permd = { 'r' : os.R_OK , 'w' : os.W_OK, 'x' : os.X_OK}  # dict for read, write & execute
         pkeys = permd.keys()
         pkeys.sort()
         pkeys.reverse()

         # confine its check to be for only all known perm types
         for aperm in 'rwx':
             if os.access(file, permd[aperm]):  # if the file can be accessed by the os_code
                perms +=  aperm   # set perm to that respective permdict key
             else:
                 perms += '-'     # else set it to - indicating none


         if isinstance(args, IOError):
             myargs = []
             myargs.extend([arg for arg in args ])
         else:
             myargs = list(args)

         myargs[1] = "'%s' %s perms: %s" % (mode, args[1], perms)

         myargs.append(arg.filename)

    else:
        myargs = args

    return tuple(myargs)

def myconnect(sock, host, port):
    try:
        sock.connect((host, port))
    except socket.error, args:
        myargs = updArgs(args)  # convert this instance to a tuple
        if len(myargs) == 1:
            myargs = (errno.ENXIO, myargs[0])  # set the tuple to this single value

        raise NetworkError, updArgs(myargs, host + ':' + str(port))

def myopen(file, mode='r'):
    try:
        f = open(file, mode)
    except IOError, args:
        raise FileError, fileArgs(args)
    finally:
        f.close()

    return f

def testfile():
    fn = tempfile.mktemp()
    fin = open(fn, 'w')
    fin.close()

    for eachtest in ((0,'r'), (0100, 'r'), (0400, 'w'), (0500, 'w')):
        try:
            os.chmod(fn, eachtest[0])
            fo = myopen(fn, eachtest[1])
        except FileError, args:
            print "%s :: %s" % (args.__class__.__name__, args)
        else:
            print "File opened .... permissions ignored"
            fo.close()
    os.chmod(fn, 0777)
    os.unlink(fn)


def testnet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # first create a socket object with a defined domain and type
    for eachLink in ('deli', 'www'):
        try:
            myconnect(s, 'deli', 8080)
        except NetworkError, args:
            print "%s ;; %s " % (args.__class__.__name__, args)

if __name__ == "__main__":
    testnet()
    testfile()






