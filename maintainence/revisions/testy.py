#!/usr/bin/env python

class DisplayNums(object):
    def chronicles(self):
        import math
        print "Numbers display in int, floor down and round ups"
        for eachNum in (.3, 2.3, 4, 3, 1.2, 2,.7,1.2,1.7,-.2,-.7,-1.2,-1.7):
            print "int(%.1f)\t%+.1f" % (eachNum, int(float(eachNum)))
            print "floor(%.1f)\t%.1f" % (eachNum, math.floor(eachNum))
            print "round(%.1f)\t%.1f" % (eachNum, round(eachNum))
            print ""
            print "--" * 10
            print ""
            pass
        pass
    
    def codec(self):
        CODEC = "utf-8"
        FILE = "file.txt"
        NOTE = u"Hello world"

        print "encoding your note"
        code = NOTE.encode(CODEC)

        t = open(FILE, 'w')
        t.write(NOTE)
        t.close()

        f = open(FILE, 'r')
        bytes = f.read()
        f.close()

        bytes_out = bytes.decode(CODEC)
        print bytes_out
        pass

    def checkeyword(self):
        import string
        alphanums = string.letters + string.digits + '_'
        loops = string.letters + "_"
        kw = raw_input("enter a python keyword === > ")
        if len(kw) > 0:
            if kw[0] not in loops:
                print "starting character must be alphabelt or underscore"
            
            else:
                import keyword as keys
                import re
                if len(kw) > 1:
                    for char in kw[1:]:
                        if char not in alphanums:
                            print "this char at ", char, " at ",  kw.index(char), " is invalid"
                            return -1

                    for x in keys.kwlist:
                        if  x == kw:
                            print "a valid python key"
                            print "Do ypi care for any notes on it"
                            return 
                        pass
                    
                else:
                    print "No identifiers found as match"
                    pass
                pass
            pass
    def showMaxFactor(self, num):
        count = num / 2
        while count > 1:
            if num % count is 0:
                print "largest factor of ", num , " is ", count
                break
            count -= 1
            pass
        else:
            print "num is prime"
            pass
        pass

    def passChecker(self):
        count= 5
        valid = False
        passes = ["independence", "freedom", "complex", "maximum",  "lobby"]
        prompt = "Enter your password to continue"
        while count > 0:
            attempts = raw_input(prompt)
            if not valid:
                for z in passes:
                    if z == attempts:
                        print "Welcome", z," to a new session"
                        valid = True
                        count = 0
                        break

                else:
                    count -= 1
                    print "wrong password "
                    print "Maximum attempts left ... ", count
                
    


        

    
                        
                  
if __name__ == "__main__":
    dp = DisplayNums()
    dp.codec()
    dp.checkeyword()
    dp.passChecker()
    for x in (18,4,4454,3,1121,12,332,292,1):
        dp.showMaxFactor(x)
    print "just checking iteration instance"
    Y = ["Niga", "oin", "ks"]
    U  = iter(Y)
    while True:
        try:
            out = U.next()
            print " '%s' found at %d " % (out, Y.index(out))
        except StopIteration as sp:
            print "....Done!..."
            break
        
        
