class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return self.a+other.a,self.b+other.b
d=A(10,20)
d1=A(20,30)
d2=A(30,20)
c=d+d1
d3=A(c[0],c[1])
print(d2+d3)


















