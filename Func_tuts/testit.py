def testFunc(func, *nkargs, **kwargs):
    """ This is a simple function debugger for a function with/out keys"""
    try:
        retVal = func(*nkargs, **kwargs)
        result = (True, retVal)
    except Exception, exe:
        print "These errors occured =>", exe
        result = (False, str(exe))
    return result

def runTest():
    """ Lets work a practical example with full debugging"""
    func = (int,float,long)
    vals = (1.342, 22.33, '23.34', '003')

    for op in func:
        print "*" * 10
        for v in vals:
            print "processing by %s(%s) " %  (op.__name__, str(v))
            reply = testFunc(op, v)

            if reply[0]:
                print "successfully completed = ", reply[1]



if __name__ == "__main__":
    runTest()
