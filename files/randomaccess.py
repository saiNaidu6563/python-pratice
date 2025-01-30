#program for Demonstrating random Access file
#tell() gives Index of File pointer
#seek() will reset the File pointer to Specified Valid Index to File Data
with open("fileopenexp4.py","r") as fp:
    print("intial index pointed by fp=",fp.tell())
    randata=fp.read(3)
    print("random data=",randata)
    print("index pointed by fp=",fp.tell())
    print("-"*50)
    fp.seek(11)
    print("index pointed by fp=",fp.tell())
    randata=fp.read(7)
    print("random data=",randata)
    print("index pointed by fp=",fp.tell())