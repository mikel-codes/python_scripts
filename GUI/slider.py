from Tkinter import *
class SliderDemo(Frame):
    def __init__(self, parent=None):
    

        Frame.__init__( self, parent)
        self.pack()
        self.var = IntVar()
        global label
        Label(self, text="Display scale", fg="brown", bg="black").pack()
        Scale(self, from_= 0, to=100,length=200, command =self.onMove, tickinterval=20).pack()
        Button(self, text="Read Scale", command=self.readScale).pack(padx=10,
                pady=10)

        pass

    def readScale(self) :

        selection = "scale is set to %s " % str(self.var.get())
        self.Label.config(text=selection)
        pass

    def onMove(self, val):
        print "on Move = ", val 
        pass
    
if __name__ == "__main__":
    sliderD = SliderDemo()
    sliderD.mainloop()


