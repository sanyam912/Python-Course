h=2*5-1
for i in range(0,h,1):
    for j in range(0,h):
        print(end=" ")
    h=h-1
    for k in range(0,i):
        print("* ",end="")
    print("*")
    
