from tkinter import *
r=Tk(className="Advance Notepad")
def h():
    print("a")
m=Menu(r)
filemenu = Menu(m)
filemenu.add_command(label="Open",command=h)
filemenu.add_command(label="Save",command=h)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=r.destroy)
m.add_cascade(label="File",menu=filemenu)

editmenu = Menu(m)
editmenu.add_command(label="Cut",command=h)
editmenu.add_command(label="Copy",command=h)
editmenu.add_command(label="Paste",command=h)
m.add_cascade(label="Edit",menu=editmenu)

r.config(menu=m)

