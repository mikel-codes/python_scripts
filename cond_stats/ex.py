import math
import sys
import string

debug = True

l = int(raw_input(" Enter a step-wise count for the numbers ").strip(), base=10)
j = int(raw_input(" Enter a minimum num:ber ").strip(), base=10)
k = int(raw_input(" Enter a maximum number ").strip(), base=10)

print " Representing all input in while loop "

for i in range(j, k, l):
    print i,
    pass
pass

print " "
while (j <= k):
    print j,
    j += l
    pass
pass
def o4i():
    print "Sample Output"
    bV = int(raw_input(" Enter a begin value "), base = 10)
    eV = int(raw_input(" Enter a end Value "), base = 10)
    print "DEC    BIN     OCT     HEX"
    print ('-' * 28)
    while bV <= eV:
        print bV,  bin(bV),   oct(bV),   hex(bV)
        bV += 1

def userNames():
    '"This checks for user inputs and works to keep format"'
    count = 1
    a = []
    while True:
        print "Enter a q to quit"
        ln = raw_input(" Enter your last name and firstname in the order 'Lname,Fname'").strip()
        if (ln  == 'q'):
            break
        if string.find(ln,",") > -1:
            a.append(ln)
            b = sorted(a)
        else:
            print "Invalid name format... should contain comma in between : ",count, "errors"
            count += 1
    print "Revealing the names and format"
    for x in b:
        print x

def isprime(num):
    count = int(math.sqrt(num))
    '''A prime num can be divided by itself and one without leaving a remainder
    so we test for all possible factors normally starts with its sqrt.'''
    while count >= 1:
        '''Just a single factor(must divide and leave no remainder) can make this num not prime '''
        if num % count == 0:
            print " This number is not prime"
            return False
        count -= 1
        pass
    else:
        return True
    pass
pass

def getFactors(num):
    b = []
    x = 1
    while x <= num:
        if(num % x == 0):
            b.append(x)
            pass
        x += 1
        pass
    print "All possible factors of ",num ,"are", b
    pass
pass

def isPerfect(num):
    x = []
    b = 1
    while b < num:
        if( num % b == 0 ):
            x.append(b)
            pass
        b += 1
        pass
    if ( sum(map(int,x)) == num ):
        print num, "is a perfect number"
    else:
        print "Not a perfect num "
    pass

def Factorial(N):
    return math.factorial(N)

def Fibonacci(max):
    x , y = 1, 1

    while x <= max:
        print x,
        x , y = y, x + y
        if y > max:
            print "Maximum or Nth number for Fibonacci series of ", max ," is ",x
            break


class Foo(object):
    ''' searches for a string in a text file : fgrepwc [-i] string file '''

def usage():
    "print usage and exit"
    print " Usage: fgrepwc [-i] string file "
    sys.exit(1)

def fileFind(word,filename):
    '''search for word in this file'''
    count = 0
    try:
        '''Attempt to open this file'''
        fh = open(filename,'r')
    except:
        print filename, ":", sys.exc_info()[1]
        usage()
    divide = fh.readlines()
    for eachLine in divide:
        if string.find(eachLine,word) > -1:
            count += 1
            print eachLine,
            pass
    fh.close()

def checkArgs():
    args = len(sys.argv)
    if(args != 3):
        print "Note the format below "
        usage()
    fileFind(sys.argv[1],sys.argv[2])


if __name__ == '__main__':
    isprime(48)
    getFactors(30)
    isPerfect(6)
    Factorial(5)
    Fibonacci(1000)
    foo = Foo()
    checkArgs()
    userNames()
    o4i()
