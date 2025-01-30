print("enter a value mix of all numbers and alphabets:")
n=[v for v in input()]
up=list(filter(lambda val:val.isalpha()and val.isupper() , sorted(n,reverse=True)))
lw=list(filter(lambda val:val.isalpha() and val.islower() ,sorted(n)))
ev=list(filter(lambda val:val.isdigit() and float(val)%2==0,sorted(n,reverse=True)))
od=list(filter(lambda val:val.isdigit() and float(val)%2!=0,sorted(n)))
print("given list of values=",n)
print("upper values =",up)
print("lower values=",lw)
print("even number=",ev)
print("odd numbers=",od)



