#program for accepting student data student number,name,marks and college name
import pickle
#create exception
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
        words=name.split()
        res=True
        for word in words:
            if not word.isalpha():
                res=False
                break
            if res:
                return name
            else:
                raise InvalidNameError
def studwrite():
    with open("stud.picle","ab") as fp:
        while(True):
            try:
                sno=int(input("enter student number:"))
                sname= validate(input("enter student name:"))
                marks=float(input("enter marks:"))
                clgname=validate(input("enter college name:"))
                lst=[]
                lst.append(sno)
                lst.append(sname)
                lst.append(marks)
                lst.append(clgname)
                pickle.dump(lst,fp)
                print("one student record is copied:")
                ch=input("Do u want enter another student details(yes/no):")
                if ch.lower()=="no":
                    print("thax for using")
                    break
            except ValueError:
                     print("\tDon't enter alnums,strs and symbols for sno and marks")
            except InvalidNameError:
                    print("\tInvalid  sname / clg name--try again")
            except SpaceError:
                 print("\tDon't Give Space for SName / clg name--try again")
            except ZeroLengthError:
                 print("\tU Must Enter Ur Name / clg name--try agaian")
#main program
studwrite()
