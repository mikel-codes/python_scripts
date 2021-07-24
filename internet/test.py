from os.path import splitext, dirname, isdir,exists
from os import unlink
from urlparse import urlparse
from urllib import urlretrieve
politics = urlparse("http://www.agile.com/","http://",0)
print politics
path = politics[1] + politics[2]
print "part 1 -> ", politics[1]
print "part 2 -> ", politics[2]
print path[-1]
ext = splitext(path)
print "extension 1 ->", ext[0]
print "extension- >" , ext[1]
if ext[1] == "":
    pass
ldir = dirname(path)
print ldir
if not isdir(ldir):
    print "is not a directory"
    if exists(ldir):
        unlink(ldir)
        print "just unliked that stuff"
else:
    print "dir found"

i = urlretrieve("stats.py")
print i[0]
