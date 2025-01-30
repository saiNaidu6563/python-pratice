#program for creating file by using csv files
import csv
h1=["sno","names","marks"]
records=[[100,"rossum",34.56],
        [200,"ritche",55.55],
        [300,"trvis",22.2],
        [400,"dennis",34.56],
        [500,"hunter",56.7],
        [600,"kvr",45.6]]
with open("D:\\python csv files\\stud2.csv","a") as fp:
    #creating headings

    s=csv.writer(fp)
    #creating records
    s.writerow(h1)
    s.writerows(records)
    print("csv files created-->verify")
