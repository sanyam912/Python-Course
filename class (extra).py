class dog:
    def bark(self):
        print("woof")
class cat:
    def bark(self):
        print("meow")
c=cat()
d=dog()
def hello(obj):
    obj.bark()
hello(c)
hello(d)
    
