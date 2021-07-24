from time import time, ctime
class WrapMe(object):
    def __init__(self, obj):
        self.data = obj
    def __str__(self):
        return str(self.data)

    __repr__ = __str__

    def get(self):
        return self.data
    def __getattr__(self, attr):  # help it access higher level class methods and data
        return getattr(self.data, attr)

class Time(object):
    def __init__(self, obj):
        self.__data = obj
        self.__mtime = self.__ctime = self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def get_timeval(self, t_type):
        if not isinstance(t_type, str) or t_type[0] not in 'cma':
            raise TypeError, "Illegal time string ('c' | 'm' | 'a' needed)"
        return getattr(self, '_%s__%stime' % (self.__class__.__name__, t_type[0]))

    def getimestr(self, t_type):
        return ctime(self.get_timeval(t_type))

    def set(self, obj):
        self.data = obj
        self.__mtime = self.__atime = time()

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    __repr__ = __str__ #simply make a reference to this assigning values in case of interpreter

    def __getattr__(self, attr): # setss up a delegate
        self.__atime = time()
        return getattr(self, attr)


if __name__ == '__main__':
    timer = Time("Hello")
    print timer
    print timer.getimestr('c')
    wp = WrapMe(9 + 5j)
    xp = WrapMe(['This', 'house', 'is', 'nit'])
    print wp
    xp.append("sale")
    print xp
    print wp.__dict__
    print dir(wp)
    print vars(wp)
    print wp.conjugate(), wp.real, wp.imag
    print wp.get()
    print wp.__class__
    print wp.__class__.__name__
