from tkinter import *
from tkinter import ttk

r=Tk()
u=IntVar()
a=ttk.Progressbar(variable=u)
a.pack()
a["maximum"]=100
a["value"]=40
u.set()
