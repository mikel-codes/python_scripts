#! /usr/bin/env python

import time
import math

arc = [773, 2938, 3384, 11, 128]
fx = sum(map(int, arc))
j = len(arc)
average = fx / j
print "The average of the items in list "
for item in arc:
    print item, time.sleep(0.2)
print "=", average

print "computing Pie=22/7 to several floating places"
for x in range(10):
    print round(math.pi, x)
    ++x

# data structure built by list
queue = []

def enQ():
    # Populate the queue
    nnpc = raw_input(" Enter queue values : ").strip().capitalize()
    queue.append(nnpc)

def deQ():
    # Depopulate the queue
    if (len(queue == 0)):
        print "Queue is empty"
    else:
        print "Removed[", queue.pop() , "]"

def viewQ():
    # This simply purints out the content of the queue
    print queue
    pass

def showmenu():
    # Triple quotes allows for multiiline
    prompt = """
    en(Q)ueue
    (D)equeue
    vie(W)
    (E)xit
    Enter choice: """
    done = 0
    while not done:
        choice = 0
        while not choice:
            try:
                option = raw_input(prompt).strip()[0].upper()
            except(EOFError,KeyboardInterrupt):
                option = "E"
                pass

            print "yOu picked [%s]" % option
            if option not in "QDWE":
                print "option invalid ... try again"
            else:
                choice = 1
                pass
            if option == "Q": enQ()
            if option == "D": deQ()
            if option == "W": viewQ()
            if option == "E": done = 1

if __name__ == '__main__':
    showmenu()
