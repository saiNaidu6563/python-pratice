#program for writing the data to the file
while(True):
    eno=int(input("enter employee number:"))
    ename=input("enter employee name:")
    sal=float(input("enter employee sal:"))
    with open("stud2.data","a") as fp:
        fp.write(str(eno)+"\t")
        fp.write(ename+"\t")
        fp.write(str(sal)+"\n")
        print("data wriiten to the file-- verify")
        print("-"*50)
        ch=input("Do you want insert the data(yes/no):")
        if ch.lower()=="no":
            print("thax for using program")
            break