#write the code which will accept three numerical values and find the smallest value and check for equality


a=float(input("enter the first val:"))
b=float(input("enter the second val:"))
c=float(input("enter the third val:"))
small= a if a<=b and a<c else b if b<a and b<=c else c if c<=a and c<b else "all are equal"
print("biggest value (a={},b={},c={}={}".format(a,b,c,small))