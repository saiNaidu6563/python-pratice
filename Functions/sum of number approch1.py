#program for accepting sum of numbers by using functions
#approch1
def sumof(k,v):
    c=k+v
    return c
#mainprogram
a=float(input("enter first number:"))
b=float(input("enter second number:"))
res=sumof(a,b)
print("sum({},{})={}".format(a,b,res))