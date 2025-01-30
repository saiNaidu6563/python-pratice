import csv
fn =input("enter the file name")
with open("D:\\python csv files\\"+str(fn) ,"r") as fp:
    rc=csv.reader(fp)
    for val in rc:
        for v in val:

             print(v,end="\t")
    print()