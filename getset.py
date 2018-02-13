class A:
    __a=10
    def a1(self,a):
        self.__a=a
    def a2(self):
        print(self.__a)
a=A()
a.a1(20)
a.a2()
