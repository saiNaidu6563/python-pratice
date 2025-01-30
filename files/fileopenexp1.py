#program for opening files in read mode
try:
    fp=open("stud1.data","r")
except FileNotFoundError:
    print("File Does not Exist")
else:
    print("------------------------------------")
    print("i am from else block")
    print("File Opened in Read Mode Sucessfully")
    print("Type of fp=", type(fp))
    print("Is File Closed=",fp.closed)
    print("------------------------------------")
finally:
    try:
        print("i am from finally block")
        fp.close()#Manually Closing
        print("File Closed Safely")
        print("Is File Closed=", fp.closed)
        print("------------------------------------")
    except NameError:
        print("File Not at all Opened in Read Mode--No need to close")