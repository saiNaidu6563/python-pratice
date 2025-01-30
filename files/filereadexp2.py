##program for demonstrating reading the data from files
try:
    with open("fileopenexp4.py","r") as rp:
        f=rp.readlines()
        #print(f)
        print("type=",type(f))
        for d in f:
            print(d)
except FileNotFoundError:
    print("file is not there:")