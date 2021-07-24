from urllib import urlretrieve
import sys

def firstNonBlank(lines):
    """ will return the first non-empty line it finds whether from top or bottom"""
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine

def FirstLast(webpage):
    '''call firstNonBlank on the first and last lines of html'''
    fo = open(webpage)
    extracts = fo.readlines()
    fo.close()

    print firstNonBlank(extracts)
    extracts.reverse()
    print firstNonBlank(extracts)

def download(url='http://www.earlyface.com.ng/', process=FirstLast):

    """finally get a webpage and do all"""
    try:
        page = urlretrieve(url)[0]
    except IOError,e :
        print "Webpage could not be retreived now :: ", e, sys.exc_info()
        page = None
    if page:
        process(page)

if __name__ == '__main__':
    download()
