#program for accepting numerical numbers and find sum of positive numbers and find sum of negative number
n=int(input("enter how many values you want:"))
if n<=0:
    print("{} is invalid input".format(n))
else:
    lst=[]
    for v in range(1,n+1):
        val=float(input("enter {} value:".format(v)))
        lst.append(val)
    else:
        print("given list of values")
        print(lst)
        print("*"*50)
        ps=0
        plst=[]

        for v in lst:
            if v<=0:
                continue
            plst.append(v)
            ps=ps+v
        else:
            print("positive numbers={}".format(plst))
            print("positive sum={}".format(ps))
            print("*"*50)
        nglst=[]
        ns=0
        for v in lst:
            if v>=0:
                continue
            nglst.append(v)
            ns=ns+v
        else:
            print("negative number={}".format(nglst))
            print("negative sum ={}".format(ns))


