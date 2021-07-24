a = 3
def history(a=3):
    z = 1
    print "time and space"
    print history.func_name
    print "function code base (lower levels of this module) ", history.__module__
    print "function defaults for undefined tuples ", history.__defaults__
    print "tuples of cell object that to that defines what we use here ", history.func_closure
    print history.__code__
    print type(history)

history()

class P(object):
    @classmethod
    def goo(self):
         print 'he;;p'

    def foo(self):
        print 'its here'

p = P()
print P.goo()
print p.goo()
print p.foo()

class C():
    def __call__(self):
        print "this instance is made callable"

c = C()
print c
print callable(c)
print c(), ""

