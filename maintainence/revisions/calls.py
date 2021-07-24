import sys
def closure():
    print "hello world"
    def history():
        print "the name of this function is => ", history.func_name
        print "the default args to this function is -< ", history.__defaults__
        print "function code is ", history.__code__, " and function closure is "
        print history.func_closure
        pass
    pass


class P(object):
    @classmethod
    def gold(self):
        print "this is a class method"
        pass

    def cool(self):
       print "this is an instance method"

    def __call__(self):
        print "this class instance has been made callable"
        pass


def countdown(objective):
    from time import sleep
    real = objective
    ERASE_LINE = '\033[K'
    CURSOR_UP = '\033[F'
    while objective > 0:
        if objective == real:
            print ERASE_LINE + "Duration: {0}s".format(objective)
        else:
            print CURSOR_UP  + ERASE_LINE + "Duration: {0}s".format(objective)
            pass
        sleep(0.3)
        
        objective -= 1


if __name__ == '__main__':
    closure()
    p = P()
    countdown(20)
    print '\033[K'
    print "y"
    print '\033[F'
    try: 
        p.gold()
        P.gold()
        p.cool()
        P.cool(p)
        p()
    except Exception as e:
        print e.message
        pass
