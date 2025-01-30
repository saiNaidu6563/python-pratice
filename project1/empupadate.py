import pickle


def empupdate():
    with open("employee.info","rb") as fp:
        empno = int(input("Enter Employee Number to update emp name and sal:"))
        empname = input("Enter Ur Correct Name:")
        sal = float(input("Enter Ur New Salary:"))
        lst=[]
        while(True):
            try:
                record=pickle.load(fp)
                lst.append(record)
            except EOFError:
                break
        r=False
        for ind in range(len(lst)):
            if lst[ind][0]==empno:
                index = ind
                r=True
                break
        if r:
            lst[index][1]=empname
            lst[index][2]=sal
            with open("employee.info","wb"):
                for v in lst:
                    pickle.dump(v,fp)
                    print("\tEmployee Data Updated-Verify")
        else:
            print("\tEmployee number does not exist-can't update")

