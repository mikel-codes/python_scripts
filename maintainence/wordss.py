#!/usr/bin/env python
from time import sleep
import sys
import re

def pythonic(file):
    try:
        with open(file) as x:
            count = 0
            for ln in x.readlines():
                if not ln:
                    print "EOF reached"
                    pass
                count += 1
                pass
            return  str(count) + " lines"
    except Exception as e:
        print e.message
        pass
    finally:
        x.close()
        pass
    pass

def forums():
     lamba = raw_input("Enter in anything - ")
     counter = 0
     print "you entered the following"
     while (counter < len(lamba)):
         print lamba[counter]
         sleep(0.1)
         counter += 1
         pass
     print "Done"
     sleep(0.3)
     print "your values in reverse"
     balam = lamba[::-1]
     for char in balam:
         sys.stdout.write(char)
         sys.stdout.flush()
         sleep(0.2)
         pass
     pass
 

def enumspy():
    loud = ["we", "rule", "the", "world"]
    for num, line in enumerate(loud):
        print num, " - " , line
        pass
    pass
 
def filecomp():
    comp_y = "/root/Desktop/output.txt"
    comp_x = "/root/Desktop/pass.txt"
    with open(comp_x) as x_file:
        with open(comp_y) as y_file:
            for xln in x_file.readlines():
                for yln in y_file.readlines():
                    match = re.match(xln, yln)
                    if match is not None:
                        print "both files contains a '", match.group() , "'"
                        pass
                    pass
                pass

            xln = x_file.readline()
            yln = y_file.readline()
            for num, linex in enumerate(x_file):
                for num, liney in enumerate(y_file):
                    if not re.match(liney, linex):
                        print " Files are similar on => ", num , liney,  " of output.txt"
        y_file.close()
        pass
    x_file.close()

         



def speedofThreads():
    """Try getting through all of the wordlist using threads in one woosh"""
    import threading
    with open("/root/Desktop/rockyou.txt") as wordlist:
        wordlist.seek(2)
        counter = 0
        size = file.readlines(wordlist)
        print len(size)
        for line in wordlist.xreadlines():
            counter += 1
            print line
            pass
        pass
    print counter
       

def trendingCracks():
    command = "aircrack-ng -w /root/Desktop/rockyou.txt"
    def containedHacks():
        from threading import Threads
        processes = ""
                    
if __name__ == "__main__":
    print pythonic("/root/Desktop/rockyou.txt")
    forums()
    print " "
    enumspy()
    filecomp()
    speedofThreads()
    for x, i in enumerate(range(2)):
        for y,z in enumerate(range(1,3)):
            sys.stdout.write(str(z) +  " ")
            sys.stdout.flush()
            pass
        print "\nspace", ""
        pass

