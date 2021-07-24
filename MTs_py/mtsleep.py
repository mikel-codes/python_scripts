import thread
import re
from time import ctime, sleep


loop_st = [5, 2]
def loop(nloops, nsecs, lock):
    print "loop",nloops , " started .>", re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()
    sleep(nsecs)
    print "loop",nloops , " ended .>" ,  re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()
    lock.release()

def main():
    print "This is the main process as the heavyweigth process"
    print "started at ",  re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()

    locks = []

    loops = range(len(loop_st)) # >> [0,1]
    for i in loops:
        """ its like lock saying its now offically a lock device"""
        lock = thread.allocate_lock() # this create the padlock
        lock.acquire()                # this locks the padlock
        locks.append(lock)            # :browse confirm wa

        pass

    for i in loops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in loops:
        if locks[i].locked():
            pass
        pass
    print "end ",  re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()
    pass

if __name__ == '__main__':
    main()



