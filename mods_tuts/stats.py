class TestClassMethod:
    def foo(cs):
        print "The is a method", cs.__name__
    foo = classmethod(foo)


class TestStaticMethod:
    @staticmethod
    def foo():
        print "This is another method"
        pass


class P(object):
    'This is Parent class of child C'
    def __init__(self):  #This simply sets up initial values for created object instance
        print "This is a parent constructor"   # -> its initial value
    def goo(self):
        print "This is a parent function"
        pass

class C(P):
    'This is child class of P'
    def __init__(self):
        P.__init__(self)  # we do more by explicit imports
        super(C, self).__init__()
        print "This is a child's constructor"   # -> else overrides the initial value of parent
    def foo(self):
        super(C, self).goo()
        print "This is a child method"
        pass

class Roundfloat(float):
    def __new__(cls, val):
        return super(Roundfloat, cls).__new__(cls, round(val, 2))

class SortedDicts(dict):
    def keys(self):
        return sorted(super(SortedDicts, self).keys())
c = C()
c.foo()
print C.__bases__
p = P()
print p.goo()
z = SortedDicts((('home', 1), ('alone', 2) , ('movie', 4)))
print 'by iterator '.ljust(12), [key for key in  z]
print 'by keys() ', z.keys()
print "-----", Roundfloat(221.4232)

tcm = TestClassMethod()
TestClassMethod.foo()
tcm.foo()

tsm = TestStaticMethod()
TestStaticMethod.foo()
tsm.foo()


