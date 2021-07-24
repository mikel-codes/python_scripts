
"""Python coding type of way"""
import time
import os.path
import re
with open("/root/Desktop/simple_write.c") as fp:
    try:
        N = int(raw_input("Enter a number of lines to print from this file"))
    except ValueError:
        print "Not a Number"
    for i, line in enumerate(fp):
        if i == N:
            print "Printed all required"
            print "Total lines printed ", i
            break
        print line,
fp.close()

def Files_Accessible(filepath, mode):
    try:
        Fp = open(filepath, mode)
        Fp.close()
    except IOError as e:
        print "IOErrors encounterd {0}:{1}".format(e.errno, e.strerror)
        return False
    return True
try:
    F_name = raw_input("Enter the name of a file ")
except TypeError:
    print "Not a string"


if os.path.exists(F_name) & os.path.isfile(F_name) & os.access(F_name, os.R_OK):
    Foo = open(F_name, 'r')
    for asp in Foo:
        print asp,
else:
    print " 'Unrecognized File' "



with open("3tcnDNS") as File:
    try:
        N = int(raw_input("Enter the number of lines to read "))
    except ValueError:
        print "Not a number",

    X = "skipping commented lines"
    print "Selecting overall File contents except the hashes(#)"

    for line in File:
        if not line.startswith("#"):
            print line,
        else:
            print X, time.sleep(1)

    print "Reviewing your orders"
    for num in range(N):
        for line in File:
            line.strip()
            if not line.startswith("#"):
                print line,
            else:
                time.sleep(2)
                print X

    File.close()

def Pxe():
    """ Continuity Tests """


    with open("/root/Desktop/cewl.txt") as feedback:
        cxe = """
        Enter any key to continue
        and q/E to quit.
    """

        pat = r'(\D)'
        r = re.compile(pat)
        for i, line in enumerate(feedback, 1):
                 print line,
            if i == 4:
                print cxe

if __name__ == '__main__':
    Pxe()
