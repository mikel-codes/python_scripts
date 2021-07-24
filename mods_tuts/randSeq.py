from random import choice
class randSeq(object):
    """This class selects randomly from sequence"""
    def __init__(self, sq):
        self.data = sq
    def __iter__(self):
        return self
    def __str__(self):
        return str(self.data)
    __repr__ = __str__
    def __next(self):
        return choice(self.data)
    class AnyIter:
        def __init__(self, sq, val = False):
            self.safe = val
            self.data = iter(sq)
        def next(self, howmany = 1 ):
            retVal = []
            for i in range(howmany):
                try:
                    retVal.append(self.iter.next())
                except StopIteration:
                    if self.safe:
                        break
                    else:
                        raise
            return retVal

        pass

if __name__ == '__main__':
    rand = randSeq([3,6,7,8])
    ps =randSeq.AnyIter([2,4,5])
    print ps.next
    print rand


