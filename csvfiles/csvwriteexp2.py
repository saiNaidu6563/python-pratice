#program for creating file by using csv files
import csv
h={"pid","sname","salary"}
records=[{"pid":100,"sname":"sai","salary":3.45},
        {"pid":200,"sname":"mani","salary":4.45},
        {"pid":300,"sname":"raju","salary":2.45},
        {"pid":400,"sname":"prasanth","salary":5.45}]
with open("D:\\python csv files\\stud3.csv","a") as fp:
    rc=csv.DictWriter(fp,fieldnames=h)
    rc.writeheader()
    rc.writerows(records)
    print("records saved-->verify")
