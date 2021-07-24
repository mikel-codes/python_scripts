import Tkinter as tk
def hello(event):
    print "clicked one\n Double-click to exit app"
    pass

def quit(event):
    print "Closing this application"
    import sys; sys.exit
    pass

def click():
    global btn_flag
    btn_flag = True
    if btn_flag:
        button1.config(bg="red")
        btn_flag=False
    else:
        button1.config(bg="green")
        btn_flag=True

try:
    top = tk.Tk()
    frame = tk.Frame(top)
    frame.pack()
    photo = tk.PhotoImage("0906.jpg")
    button1 = tk.Button(frame, compound=tk.TOP, width=148, height=200, image=photo,
            text="Button 1",bg="gray"  , command=click)
    button1.pack(padx=2, pady=2)
    button1.image=photo
    widget = tk.Button(frame, text="hello world")
    widget.pack()
    widget.bind('<Button-1>', hello)
    widget.bind('<Double-1>', quit)
    top.mainloop()
except Exception as ep:
    print "errors found as ", ep, ep.message
    print ep.__doc__
    pass

    

