from random import choice

class randSeq(object):
    '''lets walk it'''
    def __init__(self, seq, safe=False):
        self.iter = iter(seq)
        self.safe = safe
    def __iter__(self):
        return self
    def next(self, count=1):
        retVal = []
        # looks through the range
        for eI in range(count):
            # checks for the most available error
            try:
                # joins end to end for pulled out values(based on set eI)
                retVal.append(self.iter.next())
                # end of the sq calls for this
            except StopIteration:
                # use this condition is set
                if self.safe:
                    break
                # otherwise just raise the exception without any actions
                else:
                    print "finished jobs"
                    raise
        return retVal

class NumStr(object):
    def __init__(self, v=0, l=''):
        self.v = v
        self.l = l

    def __str__(self):
        return '%d :: %r'% (self.v, self.l)

    def __add__(self, other):
        if not isinstance(other, NumStr):
            raise TypeError, 'Illegal type argument'
        else:
            return self.__class__(self.v + other.v, self.l + other.l)
    def __mul__(self, num):
        if not isinstance(num, int):
            raise TypeError, 'Illegal type argument'
        else:
            return self.__class__(self.v * num, self.l * num)
    def __nonzero__(self):
        return self.v or self.l
    def norm_cmp


if __name__ == '__main__':
    rd = randSeq(('elo', 'world', 'er', 'what'))
    for x in rd:
        print x

    j = randSeq([2,4,6,7,8], True)
    x = iter(j)
    for i in range(1,3):
        print i, ':', x.next(i)
