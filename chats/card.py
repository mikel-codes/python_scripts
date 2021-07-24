from random import randint
from time import ctime
import threading
import itertools as itools


#import itertools as i
count = 0
t = ""
o = itools.permutations('1328736368208210',1)
while True:
    t = ""
    for x in o:
        t += ''.join(x)
        print t
    if t == '1328736368208201':
        print "complete"
        break
    else:
        t = ""
    pass
pass




