#program for digits
d=int(input("enter a digit:"))
if d==0 :
    print("{} is zero".format(d))
if d == 1:
    print("{} is one".format(d))
if d==2:
    print("{} is two".format(d))
if d == 3:
    print("{} is three".format(d))
if d == 4:
    print("{} is four".format(d))
if d == 5:
    print("{} is five".format(d))
if d == 6:
    print("{} is six".format(d))
if d == 7:
    print("{} is seven".format(d))
if d==8:
    print("{} is eight".format(d))
if d==9:
    print("{} is nine".format(d))
if (d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]):
    print("{} is negative digit".format(d))
if d >9:
    print("{} it is number".format(d))
if (d<0) and (d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]):
    print("{} it is a negative number".format(d))
