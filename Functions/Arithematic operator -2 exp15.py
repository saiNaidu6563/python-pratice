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

def readval(op):
    print("enter two values{}:".format(op))
    a,b=int(input("enter a value:")),int(input("enter b value:"))
    return a,b
def addop():
    a,b=readval("addition")

    print("sum{},{}={}".format(a, b, a + b))

def subop():
    a, b = readval("subtraction")

    print("sub{},{}={}".format(a, b, a - b))

def mulop():
    a, b = readval("multiplication")

    print("mul{},{}={}".format(a, b, a * b))

def divop():
    a, b = readval("Division")

    print("division{}{}={}".format(a, b, a / b))
    print("division{},{}={}".format(a,b,a//b))

def mudop():
    a, b = readval("madulo division")

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
