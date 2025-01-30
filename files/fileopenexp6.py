#program for file opening in write mode
try:
    with open("stud4.data","x+") as fp:
        print("file is created at read mode only one time")
        print("\t\t type of file=",type(fp))
        print("file proprties")
        print("file is closed=",fp.closed)
        print("\t\t file name=",fp.name)
        print("\t\t file mode=",fp.mode)
        print("\t\t file is readable=",fp.readable())
        print("\t\t file is writeable=",fp.writable())
    print("Out-off with open() as Indentation")
    print("Is File Closed={}".format(fp.closed))
except FileExistsError:
    print("File already exist--try with new file name")