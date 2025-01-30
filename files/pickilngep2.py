#program for accepting employee number,name,salary,degination
import pickle
#create exceptions
class InvalidNameError(Exception):pass
class SpaceError(Exception):pass
class ZeroLengthError(Exception):pass
#use exceptions
def validate(name:str):
    if len(name)==0:
        raise ZeroLengthError
    elif name.isspace():
        raise SpaceError
    else:
        word=name.split()
        res=True
        for w in word:
            if not w.isalpha():
                res=False
                break
            if res:
                return name
            else:
                raise InvalidNameError
def savefile():
    with open("emp.pic","ab") as fp:
        while (True):
            try:
                eno=int(input("enter employee number: "))
                ename=validate(input("enter employee name:"))
                sal=float(input("enter employee salary:"))
                deg=validate(input("enter employee degination:"))
                lst=[]
                lst.append(eno)
                lst.append(ename)
                lst.append(sal)
                lst.append(deg)
                pickle.dump(lst,fp)
                print("one record is copied sucessfully")
                ch=input("do u want add another details (yes/no):")
                if ch.lower()=="no":
                    print("thax for using ")
                    break
            except ValueError:
                     print("\tDon't enter alnums,strs and symbols for Empno and salary")
            except InvalidNameError:
                    print("\tInvalid Emp Name / Designation--try again")
            except SpaceError:
                 print("\tDon't Give Space for Emp Name / Designation--try again")
            except ZeroLengthError:
                 print("\tU Must Enter Ur Name / Designation--try again")
savefile()

