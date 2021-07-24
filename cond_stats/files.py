import os
import sys
import time
import string


os.linesep = ":"
print "Total size of file is ", os.stat("words.txt").st_size
print os.curdir  # prints the current directory(.)
print os.pardir  # print parent directory(..)
f = open("words.txt", 'rU')
print f.fileno()
print f.tell()  # position of the pointer immediately after opening file
calb = [line.strip() for line in f.readlines()]  # for any operation on this object like the strip,it returns a object
x = f.tell()  # file pointer pos* after reading through now its at the end becos of calb
# using file objects as their own iterators instead of file object handling
# support methods

i = iter(f)
while True:  # returns an enumerable object
    try:
        fetch = i.next()
        print fetch,
    except(StopIteration):
        print "File limit reached ", sys.exc_info()[1]
        break

o = f.seek(0, 1)

f.close()

for line in calb:
    print line,

print x, " : ", o

# Testing filename with the 'w' mode

File = raw_input("Enter the name of your file : ")
xts = open(File, 'w+')
print xts.fileno()
while True:
    aLine = raw_input(" Enter your preferred contents to file and '.' to quit ")
    if (string.find(aLine, ".") > -1):
        break
    else:
        print "Enter your values to be written to this File"
        data = [xts.writelines("%s%s" % (aLine, os.linesep))]
        time.sleep(1)

print "Here are the File contents :"
print "File : ", File
for eachLine in data:
    print eachLine,


def os_usage():
    for tmpdir in ('/root/Desktop/ct', r'/Desktop'):
        if os.path.isdir(tmpdir):
            break
    else:
        print "Not a temp directory:"
        tmpdir = ' '

    if tmpdir:
        os.chdir(tmpdir)
        cwd = os.getcwd()
        print " Current temporary directory"
        print cwd

        print "Making an example directory"
        os.mkdir('example')
        os.chdir('example')
        cwd = os.getcwd()
        print " Current working directory ;"
        print cwd
        print " Total list of directory "
        print os.listdir(cwd)

        print " creating a test file"
        fobj = open('test', 'w')
        fobj.write('Foo \n')
        fobj.write('Bar \n')
        fobj.close()

        print "listing updated directory"
        print os.listdir(cwd)
        print os.walk(cwd)

        print " ---renaming test=> filetest.txt ----"
        os.rename('test', 'filetest.txt')
        print " Update files in directory "
        print os.listdir(cwd)

        path = os.path.join(cwd, os.listdir(cwd)[0])
        print "This is the full file pathname"
        print path

        print "pathname::basename tuple == ",
        print os.path.split(path)
        print "filename, extension == ",
        print os.path.splitext(os.path.basename(path))

        print "reading complete contents of file"
        pt = open(path)  # default mode is read
        for line in pt:
            print line,
        pt.close()

        print "removing this test file"
        os.unlink(path)  # removes file since is a file command
        print "updated directory list "
        print os.listdir(cwd)
        print " removing parent directory"
        os.chdir(os.pardir)
        os.rmdir('example')

        print "))))) DONE ((((((("

if __name__ == '__main__':
    os_usage()
