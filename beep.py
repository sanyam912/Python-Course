from tkinter import *
import webbrowser as w
import winsound
import os

r=Tk()

def a():
    winsound.Beep(6700,3)

b=Button(command=a)
b.pack()
