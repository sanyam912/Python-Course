class A:
    def a1(self):
        print("hello")
class B(A):
    def b1(self):
        print("ABC")
class C(A):
    def c1(self):
        print("abc")
class D(A):
    def d1(self):
        print("HELLO")
b=B()
c=C()
d=D()
b.a1()
b.b1()
c.a1()
c.c1()
d.a1()
d.d1()
