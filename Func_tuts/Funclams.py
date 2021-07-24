import Tkinter
from functools import partial
from random import randint
root = Tkinter.Tk() #create object
button = partial(Tkinter.Button, root, fg = "grey", bg = "brown" )
b1 = button(text = "Button 1", fg = "white")
b2 = button(text = "Button 2", fg = "brown", bg = "grey")
qb = button(text= "QUIT", command = root.quit)
b1.pack()
b2.pack()
qb.pack(fill = Tkinter.X, expand=True)
root.title("PFA's Type")
root.mainloop()

y = 3
def Foo():
    x = 3
    bar = lambda : x + y # in python functions are objects
    print bar() #calling the function as an object passed to variable bar
    x = 6
    print bar()

Foo()


j,  k = 1, 2
def proc1():
    j, k = 3,4
    print "j == %d and k == %d" % (j, k)
    k = 5
def proc2():
    j = 6
    proc1()
    print "j == %d and k == %d" % (j, k)

k = 7
proc1()
print "j == %d and k == %d" % (j, k)
j = 8
proc2()
print "j == %d and k == %d" % (j, k)


"""This is Recursion"""
def factorial(n):
    if n == 0 | n == 1:
        return 1
    else:
        return  (n * factorial(n-1))
    print "factorial(%d) = " % (n)

print factorial(7)
def simpleGen():
    yield 1
    yield "2 -> punch"

for line in simpleGen():
    print line

def randGen(aList):
    if len(aList) > 0:
        yield aList.pop(randint(0, len(aList)))

for ac in randGen(['world', 'plays', 'circle', 'of', 'fire']):
    print ac
