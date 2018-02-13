class A:
    def a1(self):
        print("hello")
class B(A):
    def b1(self):
        print("HELLO")
class C(A):
    def c1(self):
        print("abc")
class D(B,C):
    def d1(self):
        print("ABC")
d=D()
d.a1()
d.b1()
d.c1()
d.d1()
