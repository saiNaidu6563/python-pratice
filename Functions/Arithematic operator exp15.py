#program for accepting Arithematic operators by using function
def airthematic():
    print("*"*50)
    print("\t\t 1. addition")
    print("\t\t 2.subtraction")
    print("\t\t 3.multiplication")
    print("\t\t 4. division")
    print("\t\t 5.madulo division")
    print("\t\t 6. power")
    print("\t\t 7. exit")
    print("*"*50)
def addop():
    print("enter two values for addition")
    a, b = int(input()), int(input())
    print("sum{},{}={}".format(a, b, a + b))

def subop():
    print("enter two values for subtraction")
    a, b = int(input()), int(input())
    print("sub{},{}={}".format(a, b, a - b))

def mulop():
    print("enter two values for multiplication")
    a, b = int(input()), int(input())
    print("mul{},{}={}".format(a, b, a * b))

def divop():
    print("enter two values for division")
    a, b = int(input()), int(input())
    print("division{}{}={}".format(a, b, a / b))
    print("division{},{}={}".format(a,b,a//b))

def mudop():
    print("enter two values for madulo division")
    a, b = int(input()), int(input())
    print("mod{},{}={}".format(a, b, a % b))

def powop():
    a, b = int(input("enter base value:")), int(input("enter power value:"))
    print("pow{},{}={}".format(a, b, a ** b))

#main program
while(True):
    ch=(input("enter ur choice:"))
    airthematic()
    if ch.isdigit():
        match(int(ch)):
            case 1:
                addop()
            case 2:
                subop()
            case 3:
                mulop()
            case 4:
                divop()
            case 5:
                mudop()
            case 6:
                powop()
            case 7:
                print("thanks for using this program:")
            case _:
                print("u r option is wrong")
