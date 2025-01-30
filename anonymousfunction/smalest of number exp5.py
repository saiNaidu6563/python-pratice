#program for accepting smallest number and check for equality
s=lambda  a,b:a if a<b else b if b<a else "both are equal"
print("enter two numbers")
r=s(float(input()),float(input()))
print("small=",r)