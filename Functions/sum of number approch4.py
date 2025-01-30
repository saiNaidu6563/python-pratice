#program for accepting sum of numbers by using functions
#approch 4
def sumof():
    a = float(input("enter first number:"))
    b = float(input("enter second number:"))
    c=a+b
    return a,b, c
#main program

a,b,r=sumof()

print("sum({},{})={}".format(a,b,r))
print("------------OR---------------")
r=sumof() # Function call with single line --Not taking Input But returning the Resulr
#here res is an object of type <class, tuple>
print("sum({},{})={}".format(r[0],r[1],r[2]))
print("------------OR---------------")
print("sum({},{})={}".format(r[-3],r[-2],r[-1]))