#program for accepting three values and find smallest values and check for equality
t=lambda a,b,c:a if a<=b and a<c else b if b<a and b<=c else c if c<b and c<=a else  "are equal"
print("enter three values:")
a,b,c=float(input()),float(input()),float(input())
#r=t(float(input()),float(input()),float(input()))
r=t(a,b,c)
print("given three values ({},{},{})={} is small value".format(a,b,c,r))