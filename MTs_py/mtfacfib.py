import re
import threading
from threading import Thread
from time import ctime, sleep
a = []

def fib(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (fib(x - 2) + fib(x - 1))


def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x - 1))

def sum(x):
    sleep(0.2)
    if x < 2: return 1
    return (x + sum(x - 1))

l = [fib, fac, sum]
n = (5,5,5)


def main():
    threads = []
    tools = range(len(l))
    print "starting execution in main thread :- ",  re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()

    print "((()))displaying for single threading ",   re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()
    for i in tools:
        print l[i](n[i])

    print "conncluded single T's at ",   re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()

    print "***** now using MT_styles ",
    print "starting execution in main thread :- ",  re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()
    for i in tools:
        t = threading.Thread(target=l[i], args=(n[i], ))
        threads.append(t)
    for i in tools:
        threads[i].start()

    for i in tools:
        threads[i].join()
        print threads[i]
    print "conncluded multiple T's at ",   re._compile('\d\d:\d\d:\d\d', 0).search(ctime()).group()



if __name__ == '__main__':
    main()
