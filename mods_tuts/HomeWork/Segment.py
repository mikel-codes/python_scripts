

class Segment(object):
    def __init__(self, x= 0,y=0 , x1=0,y1=0):
        self.__cord1 = (x,y)
        self.__cord2 = (x1, y1)
        self.data =(self.__cord1, self.__cord2)

    def __length__(self):
        val = ((self.__cord2[1] - self.__cord1[1])**2 +  (self.__cord1[0] - self.__cord2[0])**2) ** 1/2
        return val

    def __repr__(self):
        return 'self.data'

    def __str__(self):
        return str(self.data)

    def slope(self):
        s = float(self.__cord2[1] - self.__cord1[1]) / float(self.__cord2[0] - self.__cord1[0])
        print "computing slope"
        print s

    @property
    def x(self):
        return self.__cord1[0]

    @property
    def x1(self):
        return self.__cord2[0]

    @property
    def y(self):
        return self.__cord1[1]
    @property
    def y1(self):
        return self.__cord2[1]

if __name__ == '__main__':
    d = Segment(5,4,9,7)
    print d
    d.slope()
