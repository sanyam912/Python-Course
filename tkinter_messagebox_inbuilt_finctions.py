from tkinter import *
from tkinter import messagebox as t

def b():
    t.askquestion("Question","wanna play a game?")
    
    
r=Tk()
c=Button(text="Button",command=b)
c.pack()
