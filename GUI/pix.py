from Tkinter import *
from tkMessageBox import showwarning, showerror, showinfo
from functools import partial


WARN = 'warn'
INFO = 'info'
ERR =  'err'

ROADSIGNS = { 'do not cross': WARN, 'speed limit': INFO, 'merging traffic': ERR, 'one way': INFO,  'wrong turn': ERR }

critCB = lambda: showerror('Error', "You just clicked the error button")
infoCB = lambda: showinfo("Info", "You just ckicked the info button")
warnCB = lambda: showwarning('Warn', "You just clicked the warning button")

def resize(ev=None):
    label.config(font=("Consolas -%d italic"  % scale.get()))
top = Tk()
top.geometry('499x400')
top.title("sample python gui")


label = Label(top, text="Hello", font="Consolas -18 bold")
btn = Button(top, text="Quit", command=top.quit, fg='red', bg='white')

pfa_btn = partial(Button, top) # this first creates Button(top)
err_btn = partial(pfa_btn, command=critCB, bg='white')   # this alread has a button so it Button(top, ....)
info_btn   = partial(pfa_btn, command=infoCB, fg='pink', bg='gray')
warn_btn   = partial(pfa_btn, command=warnCB, bg='goldenrod1', fg='indigo')
for eachSign in ROADSIGNS:
    sign = ROADSIGNS[eachSign]
    cmd='%s_btn(text=%r%s).pack(fill=X, expand=True)'  % (sign.title().lower(), eachSign,
                                                       '.upper()' if sign == ERR else '.title()')
    eval(cmd)


scale = Scale(top, from_=10, to=30, orient=VERTICAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)
label.pack(fill=X, expand=1)
btn.pack(fill=X, expand=1)
top.mainloop()
