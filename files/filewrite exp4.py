#program for reading the data from keyboard and write it to the file
with open("stud4.data","a") as fp:
    while(True):
        kbdata=input("enter a data from keyboard to stop the data press @:")
        if kbdata != "@":
            fp.writelines(str(kbdata)+"\n")

        else:
            print("data writen to the file -- verify")
            break