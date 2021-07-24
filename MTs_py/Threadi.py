import thread
import re
from time import ctime, sleep

#regexp = re.search("\d\d:\d\d:\d\d", ctime()).group()
def loop1():
    regexp = re.search("\d\d:\d\d:\d\d", ctime()).group()

    print "loop 1 thread start_time => ", regexp
    sleep(5)
    regexp = re.search("\d\d:\d\d:\d\d", ctime()).group()

    print "loop 1 ends at ", regexp

def loop2():
    regexp = re.search("\d\d:\d\d:\d\d", ctime()).group()

    print "loop2 is started at ",  regexp
    sleep(2)

    regexp = re.search("\d\d:\d\d:\d\d", ctime()).group()
    print "loop2 ends ", regexp

def main():
    regexp = re.search("\d\d:\d\d:\d\d", ctime()).group()

    print "Track these pointers in the single thread program Threadi.py"
    print
    print "This is main loop"
    print "<starts: ", regexp ,">"
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    regexp = re.search("\d\d:\d\d:\d\d", ctime()).group()
    sleep(5)
    print "<ends: ", regexp , ">"
    print

    pass


if __name__ == '__main__':
    main()

