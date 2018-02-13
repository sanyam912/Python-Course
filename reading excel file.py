f="1.xlsx"
g=open(f,"r")
print(g.mode)
print(g.closed)
print(g.name)
print(g.read(10))
g.close()
