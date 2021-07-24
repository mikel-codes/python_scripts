from Tkinter import Button, Label, END
from Tix import Tk, Control, ComboBox

top = Tk()
top.tk.eval('require Package Tix')
top.geometry('300x300')
lb = Label(top, text='Animals (in pairs; min: pair, max: dozen)')
lb.pack()

ct = Control(top, label='Number> ', integer=True, max=12, min=2,value=2, step=2)
ct.pack()
top.mainloop()

