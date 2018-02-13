class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __del__(self):
        print("deleted")
d=A(10,20)

