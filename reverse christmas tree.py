h=1
for i in range(0,7):
    for j in range(0,h):
        print(end=" ")
    h=h+1
    for k in range(7,i+1,-1):
        print(" *",end="")
    print(" ")
    
