#program for reading csv files
import csv
with open("D:\\python csv files\\stud2.csv","r") as fp:
    rc=csv.reader(fp)
    print("*"*50)
    for v in rc:
        for val in v:
            print(val,end="\t\t")
        print()
