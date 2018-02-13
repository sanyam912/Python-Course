from tkinter import *
r=Tk(className="Anything")
c=Canvas(r,height=1000,width=2000,bg="blue")
c.pack()

a=PhotoImage(file="fukri.png")
a1=c.create_image(680,600,image=a)
a2=c.create_arc(100,150,200,20,fill="red",start=90,extent=180)

c.lower(a2)
r.mainloop()
