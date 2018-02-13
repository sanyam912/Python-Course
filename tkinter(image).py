from tkinter import *
r=Tk(className="Anything")
c=Canvas(r,height=1000,width=2000,bg="blue")
c.pack()

a=PhotoImage(file="ludo_dice_pic.png")
a1=c.create_image(700,400,image=a)
a2=c.create_oval(587,405,475,305,fill="red")
c.lower(a1)

r.mainloop()
