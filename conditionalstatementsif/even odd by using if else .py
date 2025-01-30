#program for positive numbers whether it is even odd
p=int(input("enter the number:"))
if p<=0 :
    print("invalid value {}".format(p))
else:
    if p%2==0:
        print("{} is even ".format(p))
    else:
        print("{} is odd ".format(p))