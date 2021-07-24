#! /usr/bin/env python
import sys
from operator import add, sub
from random import randint, choice

options = {'+' : add, '-' : sub}
mxTries = 4

def solve():
    operations = choice('-+')    # this functions should randomly select from str(seq) and return value to operatn
    nums = [randint(1,20) for i in range(2)]     # create a 3-elementarray frm this list
    ans = options[operations](*nums)   # sets the ans to this
    pr = " %d %s %d " % (nums[0], operations, nums[1])   #perform calcs
    oops = 0
    while True:
        if int(raw_input(pr)) == ans:
            print "correct"
            break
        else:
            print "incorrect"
            oops += 1
        if oops == mxTries:
            print "The correct ans is ", ans
            break

def main():
    print "Lets play Easy Math Game"
    try:
        while True:
            solve()
            opt = raw_input("Play Again? [y]").lower()
            if opt == 'n':
                   break
    except (EOFError, KeyboardInterrupt, ValueError), w:
        print "Encountered some errors ", w, sys.exc_info()

if __name__ == '__main__':
    main()
