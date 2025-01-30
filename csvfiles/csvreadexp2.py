#program for reading csv files using dictreader()
import csv
with open("D:\\python csv files\\stud3.csv","r") as fp:
    rc=csv.DictReader(fp)
    print("*"*50)
    for val in rc:
        for v,k in val.items():
            print("{}:--->{}".format(v,k))
        print()
