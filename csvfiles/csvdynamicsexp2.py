import csv

colnames=int(input("enter how many colnames you want:"))
if colnames<=0:
    print("invalid input")
else:
    colst=[]
    for val in range(1,colnames+1):
        val=input("enter:{}:colvalue:".format(val))
        colst.append(val)
    else:
        record=int(input("enter how many records you want:"))
        if record<=0:
            print("invalid input")
        else:
            rclst=[]
            for val in range(1,record+1):
                print("*"*50)
                print("enter {} record deatils".format(val))
                print("*"*50)

                dct={}
                for val in range(0,len(colst)):
                    v=input("enter {}:".format(colst[val]))
                    dct[colst[val]]=v
                print("*"*50)
                rclst.append(dct)
            else:
                filename=input("enter file names:")
                if filename.endswith(".csv"):
                    while (True):
                        with open("D:\\python csv files\\"+str(filename),"a") as fp:

                                try:
                                    r=csv.DictWriter(fp,fieldnames=colst)
                                    r.writeheader()
                                    r.writerows(rclst)
                                    print("file is created sucessfuly-->verify")
                                    break
                                except FileNotFoundError:
                                    print("file does not exist")
                else:
                    print("invalid input")


