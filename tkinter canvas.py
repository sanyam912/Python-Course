from tkinter import *
r=Tk()
w=Canvas(r,width=200,height=100)
w.pack()
w.create_line(-15,-6,210,98,fill="black",width=2)
w.create_line(0,98,210,3,fill="black",width=2)
w.create_rectangle(60,30,150,70,fill="blue")
w.create_rectangle(70,40,140,60,fill="red")




