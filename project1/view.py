import pickle
def view():
    empno=int(input("enter employee number:"))
    lst = []
    with open("employee.info","rb") as fp:

        while(True):
            try:
                record=pickle.load(fp)
                lst.append(record)
            except EOFError:
                break
        res="not found"
        for emrec in lst:
            if emrec[0]==empno:
                res="found"
                rec=emrec
        if res=="found":
            print("*"*50)
            print("employe number:{}".format(rec[0]))
            print("employe name:{}".format(rec[1]))
            print("employe salary:{}".format(rec[2]))
            print("*"*50)
        else:
            print("\t{} Employee Number Does not Exist".format(empno))
def viewall():
    with open("employee.info","rb") as fp:
        print("-"*50)
        print("employee records")
        print("-"*50)

        while(True):
            try:
                rec=pickle.load(fp)
                for val in rec:
                    print(val,end="\t\t")
                print()
            except EOFError:
                break

