from tkinter import *
def sel():
    selection = "Value = " + str(var.get())
    label.config(text = selection)

r=Tk()

var = DoubleVar()
scale = Scale(r,from_=10,to=17,variable=var,orient=HORIZONTAL)
scale.pack(anchor=CENTER)

button = Button(r,text="Get scale value",command=sel)
button.pack(anchor=CENTER)
label = Label(r)
label.pack()
