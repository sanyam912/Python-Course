from tkinter import *
import tkinter.messagebox
import tkinter

top = Tk()
mb = Menubutton(top,text="condiments", relief=RAISED)
mb.grid()
mb.menu = Menu(mb)
mb["menu"] = mb.menu

mayoVar=IntVar()
ketchVar=IntVar()

mb.menu.add_checkbutton(label="mayo",variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup",variable=ketchVar)

mb.pack()
