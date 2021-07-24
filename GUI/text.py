import Tkinter as tk
import tkMessageBox

def callback(event):
    tkMessageBox.showinfo("Hello world from tk_message Box")
    pass

top = tk.Tk()
v = tk.StringVar()
RADIOS=['rad1', 'rad2', 'rad3', 'rad4']
var = tk.IntVar()
frame = tk.Frame(top)
frame.config(relief=tk.RAISED, borderwidth=5)
frame.pack()
label = tk.Label(frame, textvariable=v).pack()
b1 = tk.Button(top, text="display something", bg = "violet", fg="gold",height=22, width=19)
e = tk.Entry(frame)
e.pack()
def showOff():
    tkMessageBox.showinfo(e.get())
    pass
def cb():
    print "variable is ", var.get()
    pass
def rb():
    print "radio is ", v.get()
    pass
def sel():
    selection = "You selected radio -> ", str(var.get())
    radioLabel.config(text=selection)

checkbox = tk.Checkbutton(frame, text="Enable ", variable=var, command=(lambda: cb()))
checkbox.pack()

ebtn = tk.Button(frame, text="<echo field>", command=showOff, fg="green",
        bg="white")
ebtn.pack()
count = 0
for radio in RADIOS:
    radio = tk.Radiobutton(frame, text=radio , variable=var, value = count, command=(lambda: sel()))
    count += 1
    radio.pack()
    pass

radioLabel = tk.Label(frame, text="Radio options reader")
radioLabel.config(font=("Consolas", 10))
radioLabel.pack()
w = tk.Scale(frame, from_=0, to=200, orient=tk.HORIZONTAL)
w.pack()

b1.bind('<Button-1>', callback)
b1.pack(fill=tk.X, expand=1)
b1.place(bordermode=tk.OUTSIDE)
b = tk.Button(frame, text="close x", command=top.quit, bg="indigo" , fg="white")
b.pack(fill=tk.Y, expand=0)
v.set("Hello world")
print v.get()
top.mainloop()
