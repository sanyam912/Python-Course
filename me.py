from tkinter import *
from tkinter import messagebox as t

def b():
    t.showwarning("10","20")
    
    
r=Tk()
c=Button(text="Button",command=b)
c.pack()
