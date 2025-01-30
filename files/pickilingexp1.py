#program for accepting employee number,name,salary,degination
import pickle
with open("emp.pic","ab") as fp:
    while (True):
        eno=int(input("enter employee number: "))
        ename=(input("enter employee name:"))
        sal=float(input("enter employee salary:"))
        deg=input("enter employee degination:")
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


