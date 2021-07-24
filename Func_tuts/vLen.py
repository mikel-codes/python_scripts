from random import randint

def tupleVarArgs(arg1, arg2= 'blank', *theTuple):
    len = 0
    """this function checks variable arguments based on lengths """
    print "************ Presently tuple elaborated variable args **************"
    print "Function\'s first is ", arg1
    print "Funx second is ", arg2
    for var in theTuple:
        print "additional args %d " % (len), str(var)
        len = len + 1
    pass


def dictVarArgs(arg1, arg2='default', **theDict ):
    """This function uses a keyword(dictionary) variable argument length"""
    len = 0
    print "************ Presently dictionary elaborated variable args **************"
    print "Function\'s first is ", arg1
    print "Funx second is ", arg2
    for var in theDict:
        print "additional args %d for key " % (len), str(var), "=", str(theDict[var])
        len = len + 1


def selectNums():
    seq = []
    for x in range(9):
        seq.append(randint(1,99))
    return filter(lambda x: x % 2, seq)

if __name__ == '__main__':
    tupleVarArgs(10,'world wide' ,'90', 90, 'hello world')
    dictVarArgs(10,30,c=39,b=383,x=33,jo=2)
    x = selectNums()
    print x

