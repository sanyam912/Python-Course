class A:
    def a1(self):
        print("hello")
class B(A):
    def a1(self):
        print("hello ABC")
b=B()
b.a1()
