class DcvNull(object):
    def __set__(self, obj, value):
        pass

    def __get__(self, obj, typ=None):
        pass

class DcvUse(object):
    foo = DcvNull()

class DecNull(object):
    def __init__(self, name=None):
        self.name = name

    def __set__(self, obj, val): # default assigment if any else we bekom constructor
        print "Setting :%s: to ['%r'] " % (self.name, val)

    def __get__(self, obj, typ=None):
        print "Accessing the [%s] .... ignoring " % (self.name)

class DecNullUse(object):
    c = DecNull('hope')

if __name__ == '__main__':
    c = DcvUse()
    b = DecNullUse()
    x = b.c

