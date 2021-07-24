from threading import Thread
from Queue import Queue
from random import randint

from time import sleep
# the creator functions
def writeToQ(queue):
    print "putting objects in store"
    queue.put("goods", 1)
    print "store contains %d good(s)" % (queue.qsize())
    print " "

def readFrmQ(queue):
    print "consuming a good from the store"
    val = queue.get(1)
    print "store size after consumption is %d " % queue.qsize()
    print " "

# automate the functions created

def autoWriter(queue,loop):
    for x in range(loop):
        writeToQ(queue)
        sleep(randint(1,3))

def autoReader(queue,loop):
    for x in range(loop):
        readFrmQ(queue)
        sleep(randint(2,5))

funcs=[autoWriter, autoReader]
n = range(len(funcs))

def main():
    thrds =[]
    q = Queue(32)
    nloops = randint(2,5)
    a = "(((((Welcome to the queue with thread process())))"
    for i in a:
         sleep(0.3)
         print i,


    for i in n:
        t = Thread(target=(funcs[i]), args=(q, nloops))
        thrds.append(t)

    for i in n:
        thrds[i].start()
    for i in n:
        thrds[i].join()

    print "Done"

if __name__ == '__main__':
    main()

