from tkinter import *
from tkinter.ttk import *
r=Tk(className="anything")
class A:
    def __init__(self):
        self.n=Notebook(r)
        self.t=Frame(self.n)
        self.b=Button(self.t,text="Add",command=self.e)
        self.b.grid(row=1,column=2)
        self.g=1
    def e(self):
        self.g=self.g+1
        self.n.add(Text(),text="New Tab")
        print(self.g)
    def start(self):
        self.n.add(self.t,text="tab")
        self.n.grid(row=1,column=1)
k=A()
k.start()
        




