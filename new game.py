import random
def a():
    s=random.randint(1,10)
    print(s)
def b():
    a()
    print("Is this the number you thought in your mind?")
    b.c=input("Give you answer in yes or no - ")
    if(b.c=="yes"):
        d()
    elif(b.c=="no"):
        b()
    else:
        print("Please write the answer in yes or no")
        b()
def d():
    print("Do you want to play again?")
    d.v=input("Press y or n - ")
    if(d.v=="yes"):
        b()
    elif(d.v=="no"):
        print("see you next time")
    else:
        print("Please write the answer in yes or no")
        d()
def e():
    b()
e()
    
        
        
        
    
    
    
    
    
