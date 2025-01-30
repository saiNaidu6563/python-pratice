#program for creating csv files by using dictwriter()
import csv
hn={"pno","product","price"}
precords=[{"pno":100,"product":"phone","price":3000},
          {"pno":200,"product":"vegtables","price":300},
          {"pno":300,"product":"laptops","price":40000},
          {"pno":400,"product":"tshirts","price":400},
          {"pno":500,"product":"watch","price":500},
          {"pno":600,"product":"grosary","price":200}]
with open("D:\\python csv files\\prod.csv","a") as fp:
    pv=csv.DictWriter(fp,fieldnames=hn)
    pv.writeheader()
    pv.writerows(precords)
    print("csv files created sucessfully-->verify")