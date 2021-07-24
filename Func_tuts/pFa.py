from functools import partial  #these tools help for customization of function
from operator import add, mul
import Tkinter

addQ = partial(add, 10)
mul100 = partial(mul, 100)
print addQ(20)
print mul100(18)

baseTwo = partial(int, base=2)
baseTwo.__doc__  = "converts to base 10 a binary"
print baseTwo('10001')

root = Tkinter.Tk()
Button = partial(Tkinter.Button, root, fg = "red", bg = "blue")
b1 = Button(text="Button 1", fg = "green")
b2 = Button(text= "Button 2", fg = "brown")
qb = Button(text= "QUIT", command= root.quit)
b1.pack()
b2.pack()
qb.pack(expand=True, fill=Tkinter.X)
root.title("Fun with PFA's")
root.mainloop()

bar = 1
def Foo():
    print "calling Foo() in __main__"
    global bar
    bar = 100
    print "Note any changes after"

print "value of bar before Foo ", bar
Foo()
print "value of bar after Foo()", bar


