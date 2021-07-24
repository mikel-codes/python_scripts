#! /usr/bin/env python
"fgrepwc.py -- searches for string in text file"
import sys
import string

# print usage n' exit
def usage():i
    print "usage: fgrepwc [-i] string file"
    sys.exit(1)
    pass
pass

# this does the main work
def filefind(word,filename):
    "Reset word count "
    count = 0
    try:
        """Attempt to open file for reading"""
        fh  = open(filename,'r')

    # if not ,exit
    except:
        print filename,":",sys.exc_info()[1]
        usage()
        pass
    allLines = fh.readlines()
    fh.close()
    for eachLine in allLines:

        # search eachline for the word
        if string.find(eachLine,word) > -1:
            count = count + 1
            print eachLine
            pass
        # when search complete print word and its count
        # print count
        pass
    pass

"""Checks for arguments validation by comparison"""
def checkargs():
    argc = len(sys.argv)
    if(argc != 3):
        usage()
        pass
    filefind(sys.argv[1],sys.argv[2])
    pass

if __name__ == '__main__':
    checkargs()

