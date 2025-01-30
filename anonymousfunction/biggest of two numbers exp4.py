#program for accepting biggest of two numbers
b=lambda  a,b:a if a>b else b if b>a else "both are equal"
print("enter two numbers")
r=b(float(input()),float(input()))
print("big=",r)