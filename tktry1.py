from Tkinter import *
import tkMessageBox
import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=10,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter query here.")

        button = Tkinter.Button(self,text=u"Submit",
                                command=self.OnButtonClick)
        button.grid(column=2,row=18)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"User Query !")

        #top = Tkinter.Tk()
        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        C1 = Tkinter.Checkbutton(self, text = "withstopwords", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
        C2 = Tkinter.Checkbutton(self, text = "spell", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 5)
        C1.grid(column=0, row= 14)
        C2.grid(column=2, row= 14)

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)


        

          
    def OnButtonClick(self):
        #self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
       #self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
       self.entry.focus_set()
       self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
