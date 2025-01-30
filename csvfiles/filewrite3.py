import csv
hn=["tno","names","salary"]
trrcords=[[100,"sai","3000"],
          [200,"mani","4000"],
          [300,"priya","5000"],
          [400,"srinu","6000"],
          [500,"teju","3000"]]
with open("D:\\python csv files\\stud4.csv","a") as fp:
    tc=csv.writer(fp)
    tc.writerow(hn)
    tc.writerows(trrcords)
    print("csv files created sucessfully-->verify")