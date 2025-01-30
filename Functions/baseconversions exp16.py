#program for accepting Base conversions by using functions
def basemenu():
    print("*"*50)
    print("BASE CONVERSIONS:")
    print("*"*50)
    print("\t\t 1. D TO B"
                    "D TO O"
                    " D TO H")
    print("\t\t 2. B TO D"
                    "B TO O"
                    "B TO H")
    print("\t\t 3. O TO D"
                    "O TO B"
                    "O TO H")
    print("\t\t 4. H TO D"
                    "H TO B"
                    "H TO O")
    print("\t\t 5. exit")

def d():
    print("enter the decimal value:")
    a = int(input())
    print("decimal :{}=(binary:{}), (oct:{}),(hex:{})".format(a, bin(a), oct(a), hex(a)))
def b():
    print("enter the binary number:")
    B = input()
    b = int(B, 2)
    print("\tbinary: {}=( decimal:{}),(oct:{}),(hex:{})".format(B,  int(b), oct(b), hex(b)))

def c():
    print("enter the oct number:")
    o = input()
    c = int(o, 8)
    print("\t oct:{} = (decimal:{}),(bin:{}),(hex:{})".format(o,c,bin(c), hex(c)))

def h():
    print("enter the hexa number:")
    h = input()
    d = int(h, 16)
    print(" \thexa: {}= (decimal:{}),(bin:{}),(oct:{})".format(h, d, bin(d), oct(d)))

#main program
while(True):
    basemenu()
    ch= int(input("enter ur choice:"))
    match (ch):
        case 1:
            d()
        case 2:
            b()
        case 3:
            c()
        case 4:
            h()
        case 5:
            print("thx for using")
            break
        case _:
            print("ur option is wrong")


