#write a code  which will accept numerical values wether it positive or negative or zero
a=float(input("enter the numerical values:"))
if(a>0):
    print("{} is positive".format(a))
if(a<0):
    print("{} is negative".format(a))
if(a==0):
    print("{} all are equal".format(a))