from time import time  #import module for time-tracking
def logged(when):   #this function loggs our function in the following ways
    def logger(f, *args, **kwargs): # defined by its closed function
        print '''
        Called:
            function: %s
                args : %r
                    kwargs: %r
        '''  % (f, args, kwargs)
    def prelogged(f):
        def wrapper(*args, **kwargs):
            logger(f, *args, **kwargs)
            return f(*args, **kwargs)
        return wrapper
    def postlogged(f):
        def wrapper(*args, **kwargs):
            now = time()
            try:
                return f(*args, **kwargs)
            finally:
                logger(f, *args, **kwargs)
                print 'time Frame shows ', (time() - now)
        return wrapper
    try:
        return {"pre" : prelogged, "post": postlogged}[when]
    except KeyError, e:
        print "This function can only return function logs using <post> or <pre>"

#finally decorate a function with this behaviour of the above

@logged("pre")
def www(name="lafia"):
    print "hello world wide + " , name

if __name__ == "__main__":
    www(name="web")

