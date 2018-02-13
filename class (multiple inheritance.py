class A:
    def a1(self):
        print("hello")
class B:
    def b1(self):
        print("HELLO")
class C(A,B):
    def c1(self):
        print("Hello")
c=C()
c.a1()
c.b1()
c.c1()
