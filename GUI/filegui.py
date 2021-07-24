import os
from Tkinter import *
from time import sleep

class DirList(object):

    def __init__(self, initDir=None):
        self.top = Tk()
        self.top.title("file viewer app")
        self.label = Label(self.top,  text="Directory Viewer v1.0")
        self.label.pack()

        self.cwd = StringVar(self.top)   # current working directory(returns string_like object) on the main object
        self.dir1 = Label(self.top, fg='red', bg="gray", font="Consolas 12 bold")
        self.dir1.pack()

        self.dirFrm = Frame(self.top)  # create a object of type Frame to hokd something
        self.dirscrollbar = Scrollbar(self.dirFrm)  # add scrollbar obj to frame(container for other widgets)

        self.dirscrollbar.pack(side=RIGHT, fill=Y) # set it vertically to the right side of frame

        self.dirs = Listbox(self.dirFrm, height=30, width=40,
                            yscrollcommand=self.dirscrollbar.set,  xscrollcommand=self.dirscrollbar.set) # scroll verticall using Scrollbar
        self.dirs.bind("<Double-1>", self.setGoDir)
        self.dirscrollbar.config(command=self.dirs.yview) # execute a verticaly view of the obj listbox
        self.dirscrollbar.config(command=self.dirs.xview)



        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirFrm.pack()

        """set for text entry for a search of dir"""
        self.dirSearch = Entry(self.top, width=30, textvariable=self.cwd)
        self.dirSearch.bind('<Return>', self.doLs)  # on enter key event pressed call the function
        self.dirSearch.pack()

        self.btmFrm = Frame(self.top)
        self.clrBtn = Button(self.btmFrm, text="clear", command=self.clrDir, fg="black", bg="white", font="Constantia 10 bold")
        self.ListBtn = Button(self.btmFrm, text="list Directory", command=self.doLs, fg="indigo", bg="white", font="Constantia 10 bold")
        self.quitBtn = Button(self.btmFrm, text="x close", command=self.top.quit, fg="gray", bg="white", font="Constantia 10 bold")
        self.clrBtn.pack(side=LEFT)
        self.ListBtn.pack(side=RIGHT)
        self.quitBtn.pack(side=RIGHT)
        self.btmFrm.pack()


        if initDir:
            self.cwd.set(os.curdir)

    def clrDir(self, ev=None):
        self.cwd.set("")

    def setGoDir(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground="gray")
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir()
        self.cwd.set(check)
        self.doLs()

    def doLs(self, ev=None):
        error = ''
        tdir = self.cwd.get()   # becoomes the text you type
        if not tdir:
            tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir + " does not exist"
        if not os.path.isdir(tdir):
            error = tdir + " :is not a directory"

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='skyblue')
            self.top.update()
            return
        self.cwd.set("Fetching Directory contents... ")
        sleep(0.1)
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        self.dir1.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachfile in dirlist:
            self.dirs.insert(END, eachfile)

        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground="skyblue")









def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
