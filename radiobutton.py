from tkinter import *
def a():
    print(var.get())
r=Tk()
var=StringVar()
var.set("U")
t=Radiobutton(variable=var,text="hello",value="A")
t.pack()
y=Radiobutton(variable=var,text="bye",value="B")
y.pack()
c=Button(text="Button",command=a)
c.pack()
