import csv
with open("D:\\python csv files\\stud4.csv","r") as fp:
    rc=csv.reader(fp)
    for val in rc:
        for v in val:
            print(v,end="\t\t")
        print()