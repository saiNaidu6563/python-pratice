#write a code which will accept  two numerical values and decided the smallest among them and check for equality
a,b=float(input("enter the values of a:")),float(input("enter the values of b:"))
if a<b:
    print("min of({},{})={} is small".format(a,b,a ))
if b<a:
    print("min of({},{})={} is small".format(a, b, b))
if a==b:
    print("min of({},{})={}".format(a, b, "both are equal"))