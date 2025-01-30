#program for accepting display the content of the data any file
try:
    filename=input("enter a file name:")
    with open(filename,"r") as rp:
        filedata=rp.readlines()
        for data in filedata:
            print(data)
except FileNotFoundError:
    print("file not exit:")
