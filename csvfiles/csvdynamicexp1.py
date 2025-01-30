#program for accepting which will create dynamic csv files
import csv

colname=int(input("enter How many colnames you want:"))
if colname<=0:
    print("invalid input")
else:
    colist=[]
    for val in range(1,colname+1):
        val=input("Enter {}:colnames:".format(val))
        colist.append(val)
    else:
        records=int(input("enter  How many records you want:"))
        if records<=0:
            print("invalid input:")
        else:
            rlst=[]
            for val in range(1,records+1):
                print("*"*50)
                print("enter {} records details:".format(val))
                print("*"*50)
                lst=[]
                for v in range(0,len(colist)):
                    val=input("Enter {}:values:".format(colist[v]))
                    lst.append(val)
                print("*"*50)
                rlst.append(lst)
            else:
                filename=input("enter file name:")
                if filename.endswith(".csv"):
                    while (True):
                        with open("D:\\python csv files\\"+str(filename) ,"w") as fp:
                                try:
                                    rc=csv.writer(fp)
                                    rc.writerow(colist)
                                    rc.writerows(rlst)
                                    print("file is created sucessfully-->verify")
                                    break
                                except FileNotFoundError:
                                    print("print file does not exist:")
                else:
                    print("invalid input")


