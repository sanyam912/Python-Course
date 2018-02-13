f="a.txt"
g=open(f,"a")
print(g.mode)
print(g.closed)
print(g.name)
g.write("hello")
g.write("ABC")
g.close()
