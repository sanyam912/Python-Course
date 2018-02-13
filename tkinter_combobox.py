from tkinter import *
from tkinter import ttk

r=Tk()
def b():
    d=a.get()
    print(d)
a=ttk.Combobox(value=('a','b'))
a.set('f')
a.pack()
c=Button(text="Button",command=b)
c.pack()

