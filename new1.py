import random
def b():
    b.s=random.randint(1,10)
    
    
def y1():
    b()
    for i in range(0,1000):
        a=int(input("enter a number between 1 and 10 - "))

        if(a<b.s):
            print("Too Low")
        
        elif(a>b.s):
            print("Too High")
        
        else:
            print("A is equal to B")
            break

y1()

def x1():
    print("Do you want to play again?")
    x1.c=input("press y or n - ")
x1()
while(x1.c=="yes"):
    b()

    if(x1.c=="yes"):
        y1()
        x1()
        
    elif(x1.c=="no"):
        print("next time")
    else:
        print("please answer in yes or no")






    

