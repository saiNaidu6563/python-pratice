#program for accepting list of numerical values and display  only negative values
n=int(input("enter a value:"))
if n <=0:
    print("{} is invalid input".format(n))
else:
    lst=[]
    for v in range(1,n+1):
        val=float(input("enter {} value:".format(v)))
        lst.append(val)
    else:
        print(lst)
        print("*"*50)
        nlst=list()
        for v in lst:
            if v>=0:
                continue
            nlst.append(v)
        else:
            print("negative values={}".format(nlst))