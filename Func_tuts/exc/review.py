from random import randint

def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1
    else:
        print "we closed down the Generator"

if __name__ == '__main__':
    print '*' * 10
    G = counter()
    print G.next()
    print G.next()
    print G.send(3)
    print G.next()
    print G.send(5)
    G.close()
    print "*" * 10

def randGen(aList):
    while len(aList) >= 0:
        try:
            yield aList.pop(randint(0, len(aList)))
        except (IndexError,StopIteration) ,e:
            print "Errors encountered ->", e
            return

for x in randGen([3,4,5,22,1]):
    print x, " "
matrix = randGen([3,4,2,23])
print matrix.next()



