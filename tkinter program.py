from tkinter import *
def b():
    c.destroy()
    d=Entry(l)
    d.pack()
    
r=Tk()
a=PhotoImage(file="fukri.png")
l=Label(image=a,height=100,width=200,bg="red")
l.pack(fill='both',expand=1)
c=Button(l,text="B",command=b)
c.pack()
