#program for area of different figures by using match case
import sys

print("*"*50)
print("Area of figures")
print("*"*50)
print("\t\t r. rectangle")
print("\t\t s. square")
print("\t\t c. circle")
print("\t\t  t. triangle")
print("\t\t e.exist")
print("*"*50)
s=input("enter your choice:")
match(s):
    case "r"|"R" :
        print("enter two numbers for rectangle:")
        l,b=float(input()),float(input())
        print("arearec({},{})={}".format(l,b,l*b))
    case "s" | "S":
        print("enter  numbers for square:")
        s = float(input())
        print("area square({})={}".format(s,s*s))
    case "c" | "C":
        print("enter two numbers for circle:")
        r= float(input())
        print("area circle({})={}".format( r,3.14*r**2))
    case "t" | "T":
        print("enter two numbers for triangle:")
        l, b = float(input()), float(input())
        print("area triangle({},{})={}".format(l, b,1/2*( l * b)))
    case "e" | "E":
        print("thanks for using this program:")
        sys.exit()

