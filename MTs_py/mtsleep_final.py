import re
from threading import Thread
from time import ctime, sleep

loops = (4,5)
class LetThread(Thread):

    def __init__(self, func, args, name=""):
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        apply(self.func, self.args)

def loop(nloop, nsecs):
    print "started executing loop",nloop, " at ", re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()
    sleep(nsecs)  # simulates a work being done
    print "completed at loop",nloop ,   re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()

def main():
    threads = []
    loop_s = range(len(loops))

    for i in loop_s:
        t = LetThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in loop_s:
        threads[i].start()                                     # brgin execution

    for i in loop_s:
        threads[i].join()                                       # wait for loop to complete its job

    print ">>> mainLoop stats : Done ",  re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()


if __name__ == '__main__':
    main()

