class Stack(object):
    global x, size
    x = []
    size = 0
    def __init__(self, item):
        #super(Stack, self).__init__()
        self.item = item
        pass

    def push(self, item):
        x.append(item)
        print "added to stack",item
        size -= 1
        return x

    def size():
        return size
    def peek(self):
        if len(x) == 0:
            print "empty"
        print x[len(x)]

    def isEmpty(self):
        print "checking state of stack (True = empty / False = has objects)"
        print [len(x) == 0]

    def pop(self):
        print "removing item"
        try:
            for i in x:
                yield 'removed'
                yield i
            size -= 1
        except IndexError, e:
            print "stack is empty", e


if __name__ == '__main__':
    stack =  Stack(9)
    stack.push(2)
    stack.isEmpty()
    for i in iter(stack.x):
        print i


