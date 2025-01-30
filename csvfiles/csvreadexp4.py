import csv


with open("D:\\python csv files\\prod.csv","r") as fp:
    rc=csv.DictReader(fp)
    for val in rc:
        for v,k in val.items():
            print("{}-->{}".format(v,k))
        print()
