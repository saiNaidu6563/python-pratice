#program for calculation temperature conversions by using anonymous function with menu drive
#aninymous function def
import sys
while(True):
        fcop=lambda F:(F-32) * (5/9)
        fkop=lambda F:(F-32)*5/9+273.15
        cfop=lambda C: (C*9/5) +32
        ckop=lambda C:C+ 273.15
        kfop=lambda K:K-273.15
        kcop=lambda K:(K - 273.15)*9/5+32



        print("*"*50)
        print("temperature conversions")
        print("*"*50)
        print("\t\t 1. F to c")
        print("\t\t 2. F to K")
        print("\t\t 3. C to F")
        print("\t\t 4. C to K")
        print("\t\t 5. K to F")
        print("\t\t 6. K to C")
        print("\t\t 7.exit")
        print("*"*50)
        c=int(input("enter you are choice:"))
        match(c):
            case 1:
                print("enter the number for coverting F to C")
                F=float(input("enter a value:"))
                print("conversion of F to C {}={}".format(F,fcop(F)))
            case 2:
                print("enter the number for coverting F to K")
                F = float(input("enter a value:"))
                print("conversion of F to K {}={}".format(F, fkop(F)))
            case 3:
                print("enter the number for coverting C to F")
                C=float (input("enter a value:"))
                print("conversion of C to F {}={}".format(C,cfop(C)))
            case 4:
                print("enter the number for coverting C to K")
                C = float(input("enter a value:"))
                print("conversion of C to K {}={}".format(C, ckop(C)))
            case 5:
                print("enter the number for converting K to F")
                K=float(input("enter the value:"))
                print("conversion of K to C {}={}".format(K,kfop(K)))
            case 6:
                print("enter the number for converting K to c")
                K = float(input("enter the value:"))
                print("conversion of K to F {}={}".format(K, kcop(K)))
            case 7:
                print("thanks for using")
                sys.exit()
            case _:
                print("u r option is wrong")

