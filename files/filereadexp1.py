#program for demonstrating reading the data from files
try:
    with open("stud2.data","r") as rp:
        f=rp.read()
        print(f)
        print("type=",type(f))
except FileNotFoundError:
    print("file is not there:")