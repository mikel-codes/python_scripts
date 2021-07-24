import Tkinter
from functools import partial

root = Tkinter.Tk() #create object
button = partial(Tkinter.Button, root, fg = "grey", bg = "brown" )
b1 = button(text = "Button 1", fg = "white")
b2 = button(text = "Button 2", fg = "brown", bg = "grey")
qb = button(text= "QUIT", command = root.quit)
b1.pack()
b2.pack()
qb.pack(expand=True, fill=)
root.title("PFA's Type")
root.mainloop()
