from tkinter import *
from tkinter import ttk
import time

r=Tk()
u=IntVar()
a=ttk.Progressbar(variable=u)
a.pack()
a["maximum"]=100
for i in range(0,100):
    time.sleep(1)
    u.set(i)
    a.update()




