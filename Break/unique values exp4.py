#program for accepting list of values dynamically from keyboard and obtain only unique values
nov=int(input("enter a number you want generate:"))
if nov<=0:
    print("{} is invalid input".format(nov))
else:
    lst=[]
    for i in range(1,nov+1):
        lst.append(float(input("enter{} value:".format(i))))
    else:
        print("list values")
        print(lst)
        unlst=list()
        for val  in lst:
            if val not in unlst:
                unlst.append(val)
            else:
                print("unique values")
                print(unlst)

