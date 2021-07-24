
from time import ctime, sleep
''' define decorators'''

seq = (1234L, 6.023e3, 900, -646)
def tsfunc(func):
    def wrapperFunc():
        ''' give this function set to outer func as argument a behaviour'''
        print "[%s] :: %s called " % (ctime(), func.__name__)
        return func()
    return wrapperFunc



@tsfunc
def Foo():
    ''' function does nothing but however has been decorated'''
    pass

def FooR():
    """ seal up a presentation foe the decorated function"""
    for i in range(3):
        Foo()
        sleep(2)


def Converter(func, seq):
    """This function *invokes built-in funcs internally"""
    return [func(eachNum) for eachNum in seq]


if __name__ == '__main__':
    FooR()
    print Converter(int, seq)
    print Converter(float, seq)
    print Converter(long, seq)
