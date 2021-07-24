#!/usr/bin/env python
import re
import string

def strcharfinder():
    inputStr = raw_input("Enter a desired string ")
    while True:

        charc = raw_input("Enter your desired char ")[0]
            
        if charc in string.letters:
            break
        pass
    
    m = re.search(charc, inputStr)
    if m:
        
        try:
            print "found ", charc, " at ", inputStr.index(charc)
        except IndexError as in_e:
            pass
    else:
        print "nothing found"
        return -1
        pass
    pass


def atoc():
    print "let me help create a complex number"
    s1 = raw_input("Enter a real part of complex number -> ")
    s2 = raw_input("Enter an imaginary part of complex number -> ")
    x1 = x2 = None
    try:
        x1 = int(s1)
        x2 = int(s2)
    except Exception as e:
        print e.message
        s1 = s2 = ""
        try:
            atoc()
        except Exception as e:
            pass
        pass
    
    print "complex number is ", complex(x1, x2)


def func_factorial(value):
    if value is 1 or value is 0:
        return 1
        pass
    
    token = value * func_factorial(value - 1)
    return token

def ave():
    from time import sleep
    import sys
    arc = [323,4423,23,1,12,2,2]
    num = len(arc)
    if num > 0:
        print "calculating average for"
        sys.stdout.write("\t")
        sys.stdout.flush()
        for item in arc:
            sys.stdout.write( str(item) + " ")
            sys.stdout.flush()
            sleep(0.1)
            pass
        print " \n\t   ----------------  \t\t"
        print "\t\t" , num
        
        print "total for average is  = ", str(sum(map(float, arc)) / float(len(arc)))


def piThree():
    from math import pi
    for x in range(8):
        print round(pi, x)



class Queue():
    queue = []

    def __init__(self):
        pass

    def enQ(self):

        data = raw_input("Enter your data into the database")
        queue.append(data)
        pass

    def deQ(self):
        
        if len(queue) is 0:
            print "Empty database"
            pass
        print "removed [ ", queue.pop() ,"]"
        pass

    def showmenu(self):
        option = """
        Q => en(Q)ueue
        D => (D)equeue
        W => vie(W)
        X => e(X)it

        Enter choice:: """

        done =  0
        print 'starting'
        while  not done:
            choice = 0
            while not choice:
                try:
                    prompt = raw_input(option).strip().capitalize()
                except (EOFError, KeyboardInterrupt):
                    prompt = "X"
                    pass

                print "You selected ", prompt

                if prompt not in "QDWX":
                    print "Invalid option selected"
                    pass
                else:

                    choice = 1
                    pass
                pass
                
            if prompt == "Q": enQ()
            if prompt == "D": deQ()
            if prompt == "W": showmenu()
            if prompt == "X": done = 1



            




if __name__ == "__main__":
    q = Queue()
    q.showmenu()

    strcharfinder()
    print func_factorial(3)
    ave()
    piThree()


