from empmenu import menu
from addemp import empadd
from deleteemp import deleteemp
from view import view,viewall
from empsearch import dsearch
from empupadate import empupdate

while(True):
    try:
        menu()
        ch=int(input("Enter you are choices:"))
        match(ch):
            case 1:
                empadd()

            case 2:
                deleteemp()
            case 3:
                empupdate()
            case 4:
                view()
            case 5:
                viewall()
            case 6:
                dsearch()
            case 7:
                print("thank's for using this program:")
                break
            case _:
                print("you are selection of option is wrong--->Try again ")
    except ValueError:
        print("Don't enter alnums, strs and special symbols")
