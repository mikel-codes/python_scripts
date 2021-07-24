class Point(object):

    def __init__(self, x=0, y=0):
       self.pts = [x,y]

    def move(self, dx, dy):
        if not isinstance(dx, (int, float)) or not (dy, (int, float)):
            print "Illegal pointer values must be a point or float"
        self.pts[0] = self.pts[0] + dx
        self.pts[1] = self.pts[1] + dy
        print "moved"

    def __setitem__(self, obj, val):
        print "updating pointer '%s' values" % obj
        self.pts[obj] = val

    def __getitem__(self, item):
        print "retreiving pointer values"
        return self.pts[item]

    def __str__(self):
        return str(self.pts)

    __repr__ = __str__

    @property
    def x(self):
        return self.pts[0]

    @property
    def y(self):
        return self.pts[1]

if __name__ == '__main__':
    p = Point()
    print p
    print p.x
    p.move(3,4)

    print p
