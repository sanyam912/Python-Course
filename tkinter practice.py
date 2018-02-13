from tkinter import *
def a():
    c1=b.get()
    r.destroy()
    h=Tk()
    g=Label(text=c1)
    g.pack()
r=Tk()
l=Label(text="A")
l.pack()
b=Entry()
b.pack()
c=Button(text="Button",command=a)
c.pack()
