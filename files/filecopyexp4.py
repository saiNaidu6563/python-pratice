#program for accepting copy the content of one file into another file
try:
    scrf=input("enter the file name which you want to copy the source file:")
    df=input("enter the  Denstination file name:")
    with open(scrf,"r")as rp:
        with open(df,"a") as wp:
            cp= rp.readlines()
            wp.writelines(cp)
            print("file is copyed:")
except FileNotFoundError:
    print("file is not exist")
