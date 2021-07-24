import os.path
from urlparse import urlparse

index_file="index.htm"
f = urlparse("www.google.com", "http:", 0)
path = f[1] + f[2]
ext = os.path.splitext(path)
if ext[1] == "":
    if path[-1]:
        path += '/'
        print path
    else:
        path += '/' + index_file
        print path
dir = os.path.dirname(path)
print dir
if os.path.sep != '/':
    dir.replace('/', os.path.sep)
    print dir
