#program for accepting employee number,name,salary,degination
import pickle
def readfile():
    with open("emp.pic","rb") as fp:
        while(True):
            try:
                v=pickle.load(fp)
                for i in v:
                    print(i,end="\t")
                print()
            except EOFError:
                print("record is not there:")
                break
readfile()
