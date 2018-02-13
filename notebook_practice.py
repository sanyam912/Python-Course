from tkinter import *
from tkinter.ttk import *
r=Tk(className="anything")
class A:
    def __init__(self):
        self.n=Notebook(r)
        self.t=Frame(self.n)
        self.b=Button(self.t,text="Add",command=self.e)
        self.b.grid(row=1,column=2)
        
    def h(self):
        print(self.n.index("current"))
    def e(self):
        
        self.n.add(Text(),text="New Tab")
        self.g=Button(self.t,text="Number Of Tabs",command=self.h)
        self.g.grid(row=2,column=2)
    def start(self):
        self.n.add(self.t,text="tab")
        self.n.grid(row=1,column=1)
k=A()
k.start()
        
