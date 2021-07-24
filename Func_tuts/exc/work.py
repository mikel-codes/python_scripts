from operator import add, mul
from functools import partial
from time import time
from urllib import urlretrieve
from random import randint
import os

def _pfa():
    '''look indepth to our examples'''
    x = int(raw_input("Enter your first num = "))
    y = int(raw_input("Enter your second num = "))

    addum = partial(add, x)
    mult =  partial(mul, x)
    print "Total answers ---"
    print "Addition ", addum(y)
    print "multiplication", mult(y)


def time_manager(timer):
    hrs = float(timer / 60)
    mins = float(timer - (hrs * 60))
    a = ("%.0f:%.0f" % (hrs, mins))

return a
def even(n):

return n % 2 == 0
def red(n,y):
    if n > y:
        return n


def gt(func, seq, init=None):
    lseq = list(seq)
    if init is None:
        res = lseq.pop(0)
    else:
        res = None
    for i in seq:
        result = func(res, i)

  return result
def average(aList):
    return float(reduce(lambda x,y :x+y, aList) / len(aList))

def FileCleaner():
    global filename
    filename = raw_input("Enter your File Name")
    prompt = raw_input('''
     Enter your choice for FileCleanUp
       1) Clean and send to a different FileCleanUp
       2) Clean within File
    ''')
    while True:
        if prompt == '1':
            def diffFile(filename):
                    fo = open(filename, 'r')
                    fi = open("output.txt", 'w')

                    for line in fo.readlines():
                        line.strip()
                        fi.writelines(line)
                    return fo
            print map(diffFile, fo)
            break;
        elif prompt == '2':

            def sameFile(filename):
                fi = open(filename, 'r+')
                for line in fi.readlines():
                    line.strip()
                    fi.writelines(line)

            print map(sameFile, filename)
            break;
        else:
            print "Invalid Selection"
            break
def timeit(func, *args, **kwargs):
    now = time()
    def testit(func, *args, **kwargs):
        try:
            retVal = func(*args, **kwargs)
            result = (True,retVal)
        except (TypeError, ValueError), diag:
            result = (False,str(diag))
        return result
    later = now - time()
    return (testit, later)
def test():
    funcs = (int, float, long)
    vals = (100, '123.4', 900,'88.9', 927.11)
    for func in funcs:
        print '*' * 10
        for val in vals:
            reply = timeit(func, val)
            if reply[0][0]: # ie we find the first value of tuple to match true
                print "%s(%s) = " % (func.__name__, `val`),reply[0][0]
                print "calcuated in secs" , reply[1]
            else:
                print "%s(%s): Failed => " % (func.__name__, `val`), reply[1]



def Factorial(N):
    seq = range(1, N+1)
    res = reduce(lambda x,y : x * y,seq)
    return res
def iteratives():
    for i in range(1, N):
        map(lambda x,y : x * y, i)
def recursions():
    prompt = raw_input("Enter a string and i will print it backwards and forwards ")
    choice = raw_input("""
        1 - Backwards
        2 - Forwards
    """)
    while True:
        if  choice == '1':
            print prompt[::-1]
            type = raw_input("Do you want to continue(y/n)").lower()
            if type == 'y':
                continue
            break
        elif choice == '2':
            print prompt[::1]
            break
        else:
            print "Your last selection was invalid"
            choice = raw_input("try again")

def binaryFactorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * binaryFactorial(n - 1))


def stringRecursions(string):
    string = raw_input("Enter a string = ")
    if len(string) == 0:
        return string[0]
    else:
        return binaryFactorial(len(string))

if __name__ == '__main__':
    _pfa()
    max2 = partial(max)
    min2 = partial(min)
    print max2(2,3)
    print min2(3,2)
    print time_manager(300)
    allNums = []
    for i in range(9):
        allNums.append(randint(1,99))
    print filter(even, allNums)
    print gt(red,"hello", 1)

    print "The average of the list numbers is %f ",  (average([2,4,5,6,7]))
    files = filter(lambda x: x and x[0] != '.', os.listdir("/root/Desktop/bluetooth"))

    print files
    print Factorial(3)
    a = []
    for x in ["Hello"]:
        print x,
        a.append(x)
    print a.__reversed__

    sas = [234,343,337474,1.9, 32,3667,86,85,30,62]
    sas.sort()
    print sas

    classic = ["Ge", "sj", "Places", "KEL", "loe"]
    print sorted([x for x in classic], reverse=False)
    print binaryFactorial(3)
    recursions()


