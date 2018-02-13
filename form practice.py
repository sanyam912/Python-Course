from tkinter import *
import tkinter
import sqlite3

r=Tk(className="Registration Form")
class A:
    def __init__(self):
        self.c=Button(text="Register",command=self.b)
        self.c.pack()

        self.k=Button(text="Login",command=self.l)
        self.k.pack()
    
    def b(self):
       self.c.destroy()
       self.k.destroy()
   
       self.d=Label(text="Name")
       self.d.grid(row=1,column=2)
   
       self.e=Entry()
       self.e.grid(row=1,column=3)

       self.f=Label(text="Email")
       self.f.grid(row=2,column=2)

       self.g=Entry()
       self.g.grid(row=2,column=3)

       self.h=Label(text="Password")
       self.h.grid(row=3,column=2)

       self.i=Entry(show="*")
       self.i.grid(row=3,column=3)

       self.j=Button(text="Register",command=self.s)
       self.j.grid(row=4,column=3)

    def l(self):
        self.c.destroy()
        self.k.destroy()

        self.m=Label(text="Email")
        self.m.grid(row=2,column=2)

        self.n=Entry()
        self.n.grid(row=2,column=3)

        self.o=Label(text="Password")
        self.o.grid(row=3,column=2)

        self.p=Entry()
        self.p.grid(row=3,column=3)

        self.q=Button(text="Login",command=self.t)
        self.q.grid(row=4,column=3)

    def s(self):
        db=sqlite3.connect('cd.db')
        cr=db.cursor()
        cr.execute(f'''insert into a1 values('{self.e.get()}','{self.g.get()}','{self.i.get()}')''')
        db.commit()

    def t(self):
        db=sqlite3.connect('cd.db')
        cr=db.cursor()
        print(self.n.get(),self.p.get())
        cr.execute(f'''select count(*) from a1 where  Email='{self.n.get()}' and Password='{self.p.get()}' ''')
        u=cr.fetchone()
        if(u[0]==0):
            print("false value")
        else:
            print("you are logged in")
        
obj=A()

    


