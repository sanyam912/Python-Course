from tkinter import *
from tkinter.ttk import *
r=Tk(className="anything")
n=Notebook(r)
n.add(Text(), text="tab 1")
n.add(Text(), text="tab 2")
n.add(Text(), text="tab 3")

n.pack()
r.mainloop()
