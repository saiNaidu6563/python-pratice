#program for writting the itearable object data to the file
x=range(10,20,2)
with open("stud3.data","a+") as fp:
    fp.writelines(str(x)+"\n")
    for i in range(20,30,2):
        fp.writelines(str(i)+"\t")

    print("data wriiten to the file-- verify")
