from time import ctime
print '!welcome to the metaclass example'
print "metaclass declaration first"

class Meta(type):
    def __init__(cls, name, bases, attrs):
        super(Meta, cls).__init__(name, bases, attrs) # metaclass default constructo


        print 'created the metaclass %r : %s' % (name, ctime())

    print "Foo class declaration is now"

class Foo(object):
    __metaclass__ = Meta
    def __init__(self):
        print "created the foo class %r : %s" % (self.__class__.__name__, ctime())
if __name__ == '__main__':
    fp = Foo()
    print fp
    print "DONE"

