#! /usr/bin/env python

import string

def findchr(inputstr,char):

    inputstr = raw_input("Enter a string ")
    char = raw_input("indicate char to be found")

    while True:
        if char in string.letters:
            break
        else:
            print "Invalid input : requires a number: "
            char = raw_input("indicate char to be found: ")
            pass

    if char in inputstr:
        print "Found char ", inputstr.index(char)
        return char
    else:
        return -1

def atoc(s1,s2):
    print "This function converts your number inputs to complex numbers "

    s1 = int(raw_input( "Enter a real number "))
    s2 = int(raw_input(" Enter a second number"))
    print "here is your complex number ", complex(s1,s2)
if __name__ == '__main__':
    findchr("Hello",'m')
    atoc('3','4')
    numbers = int(raw_input("Enter a number ").strip())
    fac_lst = range(1, numbers + 1)
    print "before: ", fac_lst
    i = 0
    while i < len(fac_lst):
        if numbers % fac_lst[i] == 0:
            fac_lst.remove(fac_lst[i])
            pass
        i = i + 1
        pass
    print "after: ", fac_lst
