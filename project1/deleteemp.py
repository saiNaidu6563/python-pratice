#deleting employee details
import pickle
def deleteemp():
    with open("employee.info","rb") as fp:
        empno=int(input("enter employee number:"))
        lst=[]
        while(True):
            try:
                rec=pickle.load(fp)
                lst.append(rec)
            except EOFError:
                break
        e=False
        for v,i in enumerate(lst):
            if (i[0]==empno):
                index = v
                e=True

        if e==True:
            lst.pop(index)

            with open("employee.info","wb") as fp:
                for r in lst:
                    pickle.dump(r,fp)
                    print("employee data deleted secessfully:")
        else:
            print("\tEmployee number does not exist-can't delete")

