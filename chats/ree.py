x = [('1','2'), ('2','2'), ('2','4')]
print x

for a, b in enumerate(x):
    if b[1] != 2:
        x.append((2,2))
        print "connect"
        break


print x

#for a, b in enumerate(x):
    #if not b[1].index(2):
     #   x.append((2,8))
      #  print "connect"
      #  break



try:
    if [b[1] for b in x].index(23):
        print "yes"
except:
    x.append((2,23))


print x

try:
    if [b[1] for b in x].index(23):
        print "yes oo"
        print b[0], b[1]
except:
    x.append((33,23))


def Joe():
    try:
        if [b[1] for b in x].index(23):
            photo()
    except:
        x.append((33,23))

def photo():
    print "okay"
    pass


print x



for a, b in enumerate(x):
    print str(a),
    print b[1]

if __name__ == '__main__':
    Joe()

