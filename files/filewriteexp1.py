#program for writing the data to the file
eno=300
ename="sai"
sal=12.5
with open("stud1.data","a") as fp:
    fp.write(str(eno)+"\t")
    fp.write(ename+"\t")
    fp.write(str(sal)+"\t")
    print("data writen to the file--verify")