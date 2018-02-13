from tkinter import *
r=Tk()
t=["G","r","p"]
var = StringVar()
w=OptionMenu(r,var,*t)
w.pack()
e=Entry(textvariable=var)
e.pack()
