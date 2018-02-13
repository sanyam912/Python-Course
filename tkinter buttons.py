from tkinter import *
import tkinter
top = tkinter.Tk()

b1= Button(top, text="flat", relief=FLAT)
b2= Button(top, text="raised", relief=RAISED)
b3= Button(top, text="sunken", relief=SUNKEN)
b4= Button(top, text="groove", relief=GROOVE)
b5= Button(top, text="ridge", relief=RIDGE)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()


e1= Button(top, text="error", relief=FLAT,bitmap="error")
e2= Button(top, text="hourglass", relief=RAISED,bitmap="hourglass")
e3= Button(top, text="info", relief=SUNKEN,bitmap="info")
e4= Button(top, text="question", relief=GROOVE,bitmap="question")
e5= Button(top, text="warning", relief=RIDGE,bitmap="warning")

e1.pack(side=LEFT)
e2.pack()
e3.pack()
e4.pack()
e5.pack()

