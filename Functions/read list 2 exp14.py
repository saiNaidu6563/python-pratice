#program for accepting read list of values and find sum and average of list
def readlst():
    n=int(input("enter a value which you want:"))
    if n<=0:
        return []
    else:
        lst=[]
        for i in range(1,n+1):
            val=float(input("enter {} value:".format(i)))
            lst.append(val)
        return lst
def sumavg():
    lst=readlst()
    if len(lst)==0:
        return "invalid input"
    else:
        print("--------------------")
        print("list of values:")
        print("---------------------")
        s=0
        for v in lst:
            print(f"\t{v}")
            s=s+v
        else:
            print("*"*50)
            print("sum={}".format(s))
            print("avg={}".format(s/len(lst)))
#main program
sumavg()