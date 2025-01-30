#program for accepting numerical numbers and get only positive even number only
num=int(input("enter how many values you want:"))
if num<=0:
    print("{} is invalid input".format(num))
else:
    lst=[]
    for v in range(1,num+1):
        val=float(input("enter {} values:".format(v)))
        lst.append(val)
    else:
        print("given list of values:")
        print(lst)
        print("*"*50)
        enlst=list()
        for v in lst:
            if v<=0:
                continue
            if v%2!=0:
                continue
            enlst.append(v)
        else:
            print("even numbers={}".format(enlst))
