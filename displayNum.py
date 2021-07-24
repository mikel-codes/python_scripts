#! /usr/bin/env python
import math

def roundNum(x):
    for eachNum in range(10):
        print round(x,eachNum)
        pass
    pass


def chronicles():
    for  eachNum in (.2,.7,1.2,1.7,-.2,-.7,-1.2,-1.7):
        print "int(%.1f)\t%+.1f" % (eachNum,float(int(eachNum)))
        print "floor(%.1f)\t%+.1f" % (eachNum,math.floor(eachNum))
        print "round(%.1f)\t%+.1f" % (eachNum,round(eachNum))

        print "-" * 20

def displayNum(x):
    print "x =>", x ,
    if type(x) == type(0):
        print 'is int '
        pass
    elif type(x) == type(0.0):
        print 'is float '
        pass
    elif type(x) == type(0L):
        print "is long Integer"
        pass
    elif type(x) == type(0+0j):
        print "is complex number",
        pass
    else:
        print "is not a number at all"
        pass
    pass
displayNum(99)
displayNum(99.9 + 9j)
displayNum(90.0)
displayNum(99L)
displayNum('xxx')

print "Now print values for numbers pi = 22/7 in several d.p"
roundNum(math.pi)

print "Finally for chronicles we have "
chronicles()
