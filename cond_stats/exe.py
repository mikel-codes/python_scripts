import os
import os.path
import re
import sys
import time
import string
from math import factorial
sep = os.linesep = ":"
def Dicts():
    """ Inspect a dictionary and adjust whats necessary """
    a = {}
    c = {'shell':'bin/bash', 'key':'value', 'star':'dust', 'directory':'silverbird'}
    for x,y in c.iteritems():
        if c.has_key('directory'):
            d = c['directory']
        else:
            d = None
        print x, y
    print d


def Analytics():
    """Checking at simple looping statements"""
    a, b = 0, 100
    while a is not b:
        a += 40
        b -= 40
        if( a % b == 0 ):
            break
        time.sleep(1)
        print ('%s%s%s' %  (a,sep,b))

    for c in "pride&love":
        print c,
    print

class Account:
    """ Reviewing Transaction and virtual accounts """
    def __init__(self, initial):
        self.balance = initial
    def deposit(self, amt):
        self.balance += amt
        print "amount deposited = %s" % (amt)
        return self.balance
    def withdraw(self, amt):
        self.balance -= amt
        print "amount withdrawn = %s" % (amt)
        return self.balance
    def getbalance(self):
        return self.balance

def factoria(N):
    if N < 0:
        raise ValueError, " Input cannot be negative "
    elif N <= 1: return 1
    else:
        return N * factorial(N - 1)


def Exceptions():
    '''place bounds in case of an error'''
    try:
        N = factorial((int)(raw_input(" input a number to know its factorial ")))
        f = open("Foo")
    except IOError:
        print "could not open file 'Foo'"
    factoria(N)

with open('oldboy') as f:
    detail = ''.join(f.readlines())
    m = re.search(r"#//\"", detail, re.S | re.M)
    if m: print m.group(1)

exe = []
Flags = False
with open('oldboy') as f:  # automatically open this file to a handler)obj(
    for line in f:  # check for line in this file
        if ( line.startswith('#') | line.startswith("\"") ):  # line needed protocols
            Flags = False  # set this off as a state for list motion

        if Flags:
            exe.append(line)  #  extends this array
        if line.strip().endswith("!"):
            Flags = False

print "".join(exe)

def strings():
    """A quick overview of python strings"""
    a = "Hello World Wide Web"
    ci = string.split(a)
    x =  string.join(["Hello","world"],':')
    y = string.replace(a, "Web", "Base ")
    print ci, x, y

def RegexF():
    """This represents regex with examples"""
    tar = r'(http:\\[\w-]+(\.[\w-]+)*((/[\w-~]*)?))'
    trade = re.compile(tar)
    trade.sub()
    a = "7123.433 Exodus 948.8484"
    pat = r'(\d+)\.(\d*)'
    r = re.compile(pat)
    m = r.match(a)
    if m:
        print "Found a match"
        print m.group(2)
        print "showing status for group 1"
        print m.start(1)  # print starting index pos for group(1)
        print m.end(1)  # print the reverse case of above
        print "showing status for group 2"
        print m.start(2)
        print m.end(2)
        print "showing overall status"
        print m.start(0)
        print m.end(0)
    else:
        print "Oops.. no match found"


def Files():
    """How to manipulate file objects"""
    sys.stdout.write("This is a file type function\n")
    sys.stdout.write("# Enter to file name to know location\n")
    sys.stdout.write(os.path.abspath("../test.csv\n"))
    sys.stdout.write(os.path.basename("../test.csv\n"))
    print os.path.basename("/lobe/life/money")
    print os.path.dirname("../test.csv")
    with open("test.csv") as f:
        with open("u.txt", 'w') as k:
            for line in f:
                k.writelines(line)
                k.tell()
            k.seek(0,20)
            k.tell()
            k.truncate(499)
        k.close()
        print f.fileno()
    f.close()

fh = open('oldboy', 'r+')
data = fh.readlines()
xtx = [ "#", "//", "\"" ]



fh.close()

if __name__ == "__main__":
    Dicts()
    Analytics()
    account = Account(1000.00)
    account.deposit(50)
    account.withdraw(200)
    print account.getbalance()
    Exceptions()
    print factorial(3)
    strings()
    Files()




