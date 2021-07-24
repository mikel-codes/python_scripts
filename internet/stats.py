from urllib import urlopen 

try:
    handler = urlopen("/root/Desktop/fike~")
    for x in handler.readlines():
        print x
    print handler.info(), handler.fileno, handler.geturl()
except Exception as e:
    print e.message
finally:
    handler.close()
