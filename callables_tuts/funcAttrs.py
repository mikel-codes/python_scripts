class Test_4Attr:
    def __init__(self):
        pass


    def foo(self):
        return True

    @staticmethod
    def goo(self):
        'go_lang programming for this language'
        return True

    foo.__doc__ = 'this is a foo function'
    foo.__tests = '''
    if foo:
        print "its Foo"
        print 'passed'
    else:
        print "Not foo"
        print 'restricted'
    '''
    pass

def Foo():
    return False

Foo.__doc__ = 'this is a foo function'
Foo.tests = '''
if Foo():
    print "its Foo"
    print 'passed'
else:
    print "Not foo"
    print 'restricted'
    '''

if __name__ == '__main__':
    test = Test_4Attr()
    print test.goo.__doc__
    print dir()
    print dir(test)
    print

    print '_' * 10
    execfile("exmp.py")
    print '_' * 10

    print
    for eachAttr in dir():
        obj = eval(eachAttr)
        if isinstance(obj, type(Foo)):
            if hasattr(obj, '__doc__'):
                print "\n%s has a doc String \n\t%r" % (eachAttr, obj.__doc__)
            if hasattr(obj, 'tests'):
                print "executing the command "
                exec obj.tests
            else:
                print "<S-F4>%s has no attribute 'tests'", eachAttr
        else:
            print "%s is not a function " % eachAttr



