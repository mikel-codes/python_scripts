# creating thread with objects

import re
import threading
from time import ctime, sleep

loops = [6,2]

class ThreadFunc(object):

    def __init__(self, func, args, name = ""):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)

def loop(nloop, nsecs):
    print "started executing loop",nloop, " at ", re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()
    sleep(nsecs)  # simulates a work being done
    print "completed at loop",nloop ,   re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()

def main():
    threads = []
    loop_s = range(len(loops))

    for i in loop_s:
        t = threading.Thread(target=ThreadFunc(loop, (i ,loops[i]), loop.__name__))
        threads.append(t)

    for i in loop_s:
        threads[i].start()                                     # brgin execution

    for i in loop_s:
        threads[i].join()                                       # wait for loop to complete its job

    print ">>> mainLoop stats : Done ",  re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()


if __name__ == '__main__':
    main()
