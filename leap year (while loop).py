i=int(input('enter starting year - '))
a=int(input('enter end year - '))
while(i<=a):
    if(i%4==0):
        if(i%100==0):
            if(i%400!=0):
                print("it is not a leap year",i)
            else:
                print("it is a leap year",i)
        else:
            print("it is a leap year",i)
    else:
        print("it is not a leap year",i)
    i=i+1

    
