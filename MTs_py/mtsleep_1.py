# creating thread passing it function and its arguments
import re
import threading
from time import ctime, sleep

loops = [4,7]
def loop(nloop, nsecs):
    print "started executing loop",nloop, " at ", re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()
    sleep(nsecs)  # simulates a work being done
    print "completed at ",  re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()

def main():
    print "invoking main thread at ",  re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()

    threads = []
    loop_stats = range(len(loops))   #>> [0,1]

    for i in loop_stats:
        t = threading.Thread(target=loop, args=(i, loops[i]))  # create the threads objects
        threads.append(t)                                     # fill up the threads database


    for i in loop_stats:
        threads[i].start()                                     # brgin execution

    for i in loop_stats:
        threads[i].join()                                       # wait for loop to complete its job

    print ">>> mainLoop stats : Done ",  re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()


if __name__ == '__main__':
    main()
