from tkinter import *
def b():
    #a()
    e=a.y.get()
    print(a.y.get())
    if(e=='j'):
        a.h.destroy()
        
def a():
    d=var.get()
    print(var.get())
    if(d=='u'):
        r.destroy()
        a.h=Tk()
        a.y=StringVar()
        a.y.set(None)
        i=Checkbutton(variable=a.y,text="bye",offvalue="k",onvalue="j")
        i.pack()
        g=Button(text="Button2",command=b)
        g.pack()
    
r=Tk()
var=StringVar()
var.set(None)
t=Checkbutton(variable=var,text="hello",onvalue="u",offvalue="b")
t.pack()
c=Button(text="Button",command=a)
c.pack()

