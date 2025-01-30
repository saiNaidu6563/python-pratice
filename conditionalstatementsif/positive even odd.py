#write a code which will accept positive value and decide whether it is even or odd
p = float(input("enter the positive value:"))
if p<=0:
    print("{}is negative only enter positive numbers".format(p))
if p>=0:
    print("{}is positive numbers".format(p))
    if p % 2 == 0 :
        print("{}is even".format(p))

    if p % 2 != 0:
        print(f"{p} is odd")
