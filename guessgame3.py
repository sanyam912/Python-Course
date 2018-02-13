import random

z="hello"
list=["_","_","_","_","_"]
def a():
    a.c=("h","e","l","l","o")
    print("Guess an alphabet")
    a.x=input()
    print(list[0])
    print(list[1])
    print(list[2])
    print(list[3])
    print(list[4])
def b():
    a()
    if(a.x==a.c[0]):
        print("Sahi")
        list[0]=a.c[0]
        a()
        b()
    elif(a.x==a.c[1]):
        print("Sahi")
        list[1]=a.c[1]
        a()
        b()
    elif(a.x==a.c[2]):
        print("Sahi")
        list[2]=a.c[2]
        a()
        b()
    elif(a.x==a.c[3]):
        print("Sahi")
        list[3]=a.c[3]
        a()
        b()
    elif(a.x==a.c[4]):
        print("Sahi")
        list[4]=a.c[4]
        a()
        b()
b()
        
    
