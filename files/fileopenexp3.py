#program for file opening in write mode
with open("stud2.data","w") as fp:
    print("file created and open in write mode")
    print("type of fp:{}".format(type(fp)))
    print("file properties")
    print("\t\t file closed=",fp.closed)
    print("\t\t file name=",fp.name)
    print("\t\t file mode=",fp.mode)
    print("\t\t file readable =",fp.readable())
    print("\t\t file writeable=",fp.writable())
print("Out-off with open() as Indentation")
print("Is File Closed={}".format(fp.closed))