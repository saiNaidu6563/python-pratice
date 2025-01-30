#adding employee data
#creating exceptions
import pickle
class InvaildNameError(EnvironmentError):pass
class SpaceError(Exception):pass
class ZeroLengthError(Exception):pass
#using exceptions
def validate(name:str):
    if len(name)==0:
        raise ZeroLengthError
    elif name.isspace():
        raise SpaceError
    else:
        w=name.split()
        res=True
        for i in w:
            if not i.isalpha():
                res=False
                break
        if res:
            return name
        else:
            raise InvaildNameError

def empadd():
    with open("employee.info","ab") as fp:
        while(True):
            try:
                print("_"*50)
                empno=int(input("enter employee number:"))
                empname=validate(input("Enter employee name:"))
                sal=float(input("enter employee salary:"))
                print("_"*50)
                lst=[]
                lst.append(empno)
                lst.append(empname)
                lst.append(sal)
               # r=unq()
                pickle.dump(lst,fp)
                print("employee details saved-->verify:")
                print("-"*50)
                ch=input("Do you want enter another employee details (yes/no):")
                if ch.lower()=="no":
                    print("thanks for using :")
                    break
            except ZeroLengthError:
                print("you must enter your name")
            except InvaildNameError:
                print("Employee name is wrong")
            except SpaceError:
                print("Don't enter space-->try again")




