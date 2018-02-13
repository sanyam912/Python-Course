try:
    x=int(input("enter first number - "))
    y=int(input("enter second number - "))
    print(x/y)
    print(z)
except ZeroDivisionError:
    print("LoL")
except ValueError:
    print("Please enter int")
except NameError:
    print("Something wrong")
