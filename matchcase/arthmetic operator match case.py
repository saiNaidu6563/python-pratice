#program for arthmetic operator for match case
import sys

print("*"*50)
print("Arthmetic operator")
print("*"*50)
print("\t\t1.Addition")
print("\t\t2.Substraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Modulo Div")
print("\t\t6.Exponentiation")
print("\t\t7.Exit")
print("*"*50)
c=int(input("enter yor choice:"))
match(c):
    case 1:
        print("enter two numbers for addition:")
        a,b=float(input("enter val of a:")),float(input("enter val of b:"))
        print("sum({},{})={}".format(a,b,a+b))
    case 2:
        print("enter two numbers for substraction:")
        a,b=float(input("enter val of a:")),float(input("enter val of b:"))
        print("sub({},{})={}".format(a,b,(a-b)))

    case 3:
        print("enter two numbers for multiplication:")
        a, b = float(input("enter val of a:")), float(input("enter val of b:"))
        print("mul({},{})={}".format(a, b, a * b))
    case 4:
        print("enter two numbers for division:")
        a,b=float(input("enter val of a:")),float(input("enter val of b:"))
        print("normal div({},{})={}".format(a, b, a / b))
        print("floor div({},{})={}".format(a, b, a // b))
    case 5:
        print("enter two numbers for madulo:")
        a,b=float(input("enter val of a:")),float(input("enter val of b:"))
        print("mod({},{})={}".format(a, b, a % b))
    case 6:
        print("enter two numbers for power:")
        a,b=float(input("enter val of base:")),float(input("enter val of power:"))
        print("pow({},{})={}".format(a, b, a ** b))
    case 7:
        print("thx for using this program:")
        sys.exit()
    case _ :
        print("Ur Selection of Operation is Wrong--try again")


