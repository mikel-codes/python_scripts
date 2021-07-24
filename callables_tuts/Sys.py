import sys
def usage():
    print "args must exceed 2 (incl, cmd name)"
    print "<usage: <script-name> <arg1> <arg2> [arg3 ...]>"
    sys.exit(1)
args = len(sys.argv)
if args < 3:
    usage()
print "total of arguments ", args
print "These are the arguments to command line(incl. script name) ", sys.argv

exec_code = compile("""
req = input("what is your name? ")

for s in req:
    print s, ":",
""", '','exec')
#exec exec_code

import re
syb = '1?kdl'
xp = '(kisooo) | locallooo'
s = re.search(syb, "Fame ooo kd l w81kdl")
y = '3.14'
z = '3\.14'
mail = '\w+@(\w+\.)?\w+\.com'
try:
    if s is not None:
        print s.group()
    else:
        raise AttributeError, "'no match found'"
    x =  re._compile(xp, 0).search("kisooo but not local").group()
    ct = re._compile(y, 0).search('3.14').group()
    bt = re.search(z, '3.14').group()
    email = re._compile(mail, 0).match("wck3@yahoo.com").group()
    giffi = re.search(mail, "oxo@oluc.com").group()
    res = re.search(r'\bthe', "Hello to the world").groups()

    print x
    print ct, bt
    print email
    print giffi
    print res
except AttributeError, e:
    print e.message,
    pass

print re.split(':', "how:are:you:")
fopen = open('/root/kol/whodata.txt', 'r+')
try:
    for x in fopen.readlines():

        fopen.writelines(re.split('\s\s+', x))
except AttributeError, e:
    print e.message
else:
    print "DoNe"

fopen.close()
from re import split
from os import popen
from sys import maxint
from time import ctime
from random import randint, choice
from string import lowercase

fp = popen('who', 'r')
for aLine in fp.readlines():
    print split('\s\s+|\t', aLine.strip())
fp.close()
print "This program generates fake data for a fake email login"
doms  =( 'com', 'gov', 'edu', 'org', 'co.uk', 'net' )

for i in range(randint(5,9)):
    dt = randint(0, maxint-1) # create a random integer between 0 - 2.pow(31)
    dtStr = ctime(1000120120120)       # create a random time string

    shorter = randint(4,7) #! shorter -->a random value
    em_type = ""   #proposed email string
    for i in range(shorter):  #as we move through shta random gen value
        em_type += choice(lowercase)  # lets concern ourselves with only lowcased alphabets

        pass

    longer = randint(shorter, 10)
    dn = ""
    for c in range(longer):
        dn += choice(lowercase)

    print "The summed up information for login at %s" % (dtStr)
    print "%s@%s.%s %d-%d-%d " % (em_type,dn, choice(doms), dt, shorter, longer)

