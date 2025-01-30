#program for accepting arthematic operation by using anonymous function with main approch
import sys
while(True):
    #anonymous functon
    addop=lambda a,b:a+b
    subop=lambda a,b:a-b
    mulop=lambda a,b:a*b
    divop=lambda a,b:a/b
    fdivop=lambda a,b:a//b
    modop=lambda a,b:a%b
    powop=lambda a,b:a**b

    print("ARTHEMATIC OPERATIONS")
    print("\t\t 1.addition")
    print("\t\t 2.subtraction")
    print("\t\t 3.multiplication")
    print("\t\t 4.Division")
    print("\t\t 5. modulo Division")
    print("\t\t 6.power")
    print("\t\t 7.exit")

    c=int(input("enter yor choice:"))
    match(c):
        case 1:
            print("enter two numbers for addition:")
            a,b=float(input("enter val of a:")),float(input("enter val of b:"))
            print("sum({},{})={}".format(a,b,addop(a,b)))
        case 2:
            print("enter two numbers for substraction:")
            a,b=float(input("enter val of a:")),float(input("enter val of b:"))
            print("sub({},{})={}".format(a,b,subop(a,b)))

        case 3:
            print("enter two numbers for multiplication:")
            a, b = float(input("enter val of a:")), float(input("enter val of b:"))
            print("mul({},{})={}".format(a, b, mulop(a,b)))
        case 4:
            print("enter two numbers for division:")
            a,b=float(input("enter val of a:")),float(input("enter val of b:"))
            print("normal div({},{})={}".format(a, b, divop(a,b)))
            print("floor div({},{})={}".format(a, b, fdivop(a,b)))
        case 5:
            print("enter two numbers for modulo:")
            a,b=float(input("enter val of a:")),float(input("enter val of b:"))
            print("mod({},{})={}".format(a, b, modop(a,b)))
        case 6:
            print("enter two numbers for power:")
            a,b=float(input("enter val of base:")),float(input("enter val of power:"))
            print("pow({},{})={}".format(a, b, powop(a,b)))
        case 7:
            print("thx for using this program:")
            sys.exit()
        case _ :
            print("Ur Selection of Operation is Wrong--try again")

