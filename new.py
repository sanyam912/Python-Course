import random
b=random.randint(1,10)
a=int (input("enter a number between 1 and 10 - "))

if(a<b):
    print("A is less than B")
elif(a>b):
    print("A is greater than B")
else:
    print("A is equal to B")
print(b)
