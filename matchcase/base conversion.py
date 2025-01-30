#program for Base conversion
print("*"*50)
print("Base conversion")
print("*"*50)
print("\t\t 1. D to B"
              "D to O"
              "D to H")
print("\t\t 2. B to D"
              "B to O"
              "B to H")
print("\t\t 3. O to D"
              "O to B"
              "O to H")
print("\t\t 4. H to D"
              "H to B "
              "H to O")
print("*"*50)
b=int(input("enter a choice:"))
# match(b):
#     case 1:
#         print(" enter a value:")
#         a =int(input())
#         print("{} decimal to binary, oct,hex ={},{},{}".format(a,bin(a),oct(a),hex(a)))
#     case 2:
#         print(" enter a binary value:")
#         B = input()
#         a=int(B,2)
#         print("{}binary to decimal{}={}".format(B,a,a))
#         print("{}binary to oct{}={}".format(B,a ,oct(a)))
#         print("{}binary to hex{}={}".format(B,a,hex(b)))
#
#     case 3:
#         print(" enter a oct value:")
#         o=input()
#         c=int(o,8)
#         print("{} oct to  decimal{}={}".format(o,c, c))
#         print("{} oct to binary{}={}".format(o,c, bin(c)))
#         print("{}oct to hex{}={}".format(o,c, hex(c)))
#     case 4:
#         print(" enter a hexa value:")
#         h=input()
#         d=int(h,16)
#         print("{} hexa to  decimal{}={}".format(h,d,d))
#         print("{} hexa to binary{}={}".format(h,d ,bin(d)))
#         print("{} hexa to hex{}={}".format(h,d, hex(d)))
#     case _:
#         print("don't enter float values")
match(b):
    case 1 :
        print("enter the decimal value:")
        a =int(input())
        print("{} decimal to binary, oct,hex ={},{},{}".format(a,bin(a),oct(a),hex(a)))
    case 2:
        print("enter the binary number:")
        B=input()
        b=int(B,2)
        print("{} binary to decimal,oct,hex {}={},{},{}".format(B,b,int(b), oct(b),hex(b)))
    case 3:
        print("enter the oct number:")
        o= input()
        c= int(o, 8)
        print("{} oct to decimal,oct,hex {}={},{},{}".format(o,c,c,bin(c),hex(c)))
    case 4:
        print("enter the binary number:")
        h = input()
        d = int(h, 16)
        print("{} binary to decimal,oct,hex {}={},{},{}".format(h,d,d,bin(d),oct(d)))
    case _:
        print("don't enter float values")





