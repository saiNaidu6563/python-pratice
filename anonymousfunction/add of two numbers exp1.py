#program for accepting two numbers and find addition of two numbers by using anonymous function
#function def
ad=lambda a,b:a+b
#main program
a,b=int(input("enter a value:")),int(input("enter b value:"))
r=ad(a,b)#function call
print("sum=",r)