f="a.txt"
g=open(f,"r")
print(g.mode)
print(g.closed)
print(g.name)
print(g.read(100))
g.close()
