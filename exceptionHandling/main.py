from division import divop
from excepts import DivisionError
try:
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    r=divop(a,b)#functioncall
except DivisionError:
    print("\t Don't enter zero for den..")
except ValueError:
    print("\t Don't enter Alnums,special symbols:")
else:
    print("\t\tdiv({},{})={}".format(a,b,r))
finally:
    print("Iam from finally block:")


#phase-3:Handling the exception