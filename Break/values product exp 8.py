#program for accepting list of values and find there product
n=int(input("enter a value you want:"))
if n<=0:
    print("{} is invalid input".format(n))
else:
    lst=[]
    for v in range(1,n+1) :
        lst.append(float(input("enter {} value:".format(v))))
    else:
        print(lst)
        print("*"*50)
        pdlst=list()

        for v in lst:
            pdlst.append(v*v)

        else:
            print("product={}".format(pdlst))

#