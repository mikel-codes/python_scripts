import Tkinter as T
class TG(T):
    def __init__(self):
        super(self)
        pass

    def quit(icon):
        print "Hello, closing the application"
        import sys; sys.exit

def hello():
    print "hello world"
top = T.Tk()

widget = T.Label(top, text="Hello world")
button  = T.Button(top, text="test", command=quit()).pack(side=T.LEFT)
button1 = T.Button(None, text="close x", command=hello).pack(side=BOTTOM)
button.bind('<Button-1>', hello)
button.bind('<Double-1>', quit)
widget.pack(side=T.LEFT)
widget.mainloop()


