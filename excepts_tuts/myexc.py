#!/usr/bin/env python
"""import all necessary modules to create our custom exception"""
import tempfile
import cmath
import math
def myopen():
    fileT = tempfile.mktemp()
    try:
        fh = open(fileT, 'w')
    except IOError, args:
        return None
    return fh


def safe_input():
    ''' Lets Try something '''
    try:
        safe = raw_input("what is your name ")
    except (EOFError, KeyboardInterrupt), exe:
        return None

    return str(safe)


def solver(a = -1):
    "'lets solve for complex numbers'"
    try:
        i = math.sqrt(a)
    except ValueError, exe:
        return None
    finally:
        x = cmath.sqrt(a)
        print "This value only results in the complex number ", x
if __name__ == "__main__":
    safe_input()
    solver()
