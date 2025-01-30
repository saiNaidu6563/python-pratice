#program for temperature conversion by using simple case
import sys

print("*"*50)
print("temperature conversions")
print("*"*50)
print("\t\t 1. F to c")
print("\t\t 2. F to K")
print("\t\t 3. C to F")
print("\t\t 4. C to K")
print("\t\t 5. K to F")
print("\t\t 6. K to C")
print("*"*50)
c=int(input("enter you are choice:"))
match(c):
    case 1:
        print("enter the number for coverting F to C")
        F=float(input("enter a value:"))
        C= (F-32) * (5/9)
        print("conversion of F to C {}={}".format(F,C))
    case 2:
        print("enter the number for coverting F to K")
        F = float(input("enter a value:"))
        K = (F-32)*5/9+273.15
        print("conversion of F to K {}={}".format(F, K))
    case 3:
        print("enter the number for coverting C to F")
        C= float(input("enter a value:"))
        F = C(9/5) +32
        print("conversion of C to F {}={}".format(C,F))
    case 4:
        print("enter the number for coverting C to K")
        C = float(input("enter a value:"))
        K = C+ 273.15
        print("conversion of C to K {}={}".format(C, K))
    case 5:
        print("enter the number for converting K to C")
        K=float(input("enter the value:"))
        C=K-273.15
        print("conversion of K to C {}={}".format(K,C))
    case 6:
        print("enter the number for converting K to F")
        K = float(input("enter the value:"))
        F = (K - 273.15)*9/5+32
        print("conversion of K to F {}={}".format(K, F))
    case _:
        print("thanks for using this program")
        sys.exit()
