#program for accepting student data student number,name,marks and college name
import pickle
def studread():
    with open("stud.picle","rb") as fp:
        while(True):
            try:
                v=pickle.load(fp)
                for i in v:
                    print(i,end="\t")
                print()
            except EOFError:
                print("no more files not there:")
                break
studread()
