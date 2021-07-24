print dir()
class Gee(object):
    def __init__(self, hr, min):
        super(Gee, self).__init__()
        print "Hello world"
        self.hr = hr
        self.min = min

    def __str__(self):
        return "%d:%d" % (self.hr, self.min)
    __repr__ = __str__
    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)
    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self
    pass


class Hee:
    foo = 100
    pass

class eodFloats(object):
    def __init__(self, val):
        assert isinstance(val, float), " The value must be a float "
        self.val = round(val, 2)  # return the instance object val modified to 2dp
        pass
    def __str__(self):
        return str(self.val)
    __repr__ = __str__
    pass


print "This is the return value as resp"
resp = eodFloats(89.82372) #creates and instantiates
resp
print resp   # a return object to 2.dp



d = Gee(4,6)
x = Gee(20,30)
print x + d
print d

h = Hee()
d.__random = 1000
setattr(h, 'pools', "goals & bets")
print hasattr(d, '__class__')
print hasattr(h, 'foo')
print hasattr(d,'__random')
print hasattr(h, 'pools')
print getattr(h, 'pools')
delattr(h, 'pools')
try:
    print getattr(h, 'pools')
except AttributeError, e:
    print "Error occured ", e

finally:
    print dir(d)
    print '*' * 10
    print dir(h)

print dir()
