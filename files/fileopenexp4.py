#program for file opening in read mode
try:
    with open("stud2.data","r+") as fp:
        print("\t\t type of file=",type(fp))
        print("file is opened in read mode")
        print("-"*20)
        print("file properties")
        print("\t\tfile is colsed=",fp.closed)
        print("\t\t file name=",fp.name)
        print("\t\t file mode=",fp.mode)
        print("\t\t file is readable=",fp.readable())
        print("\t\t file is writable=",fp.writable())
    print("Out-off with open() as Indentation")
    print("Is File Closed={}".format(fp.closed))
except FileNotFoundError:
    print("file is not there")

