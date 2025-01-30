#Python program to find second largest number in a list
s=int(input("enter a list of number:"))
if s<=0:
    print("{} is invalid input".format(s))
else:
    lst=[]
    for i in range(1,s+1):
        v=float(input("enter {} values:".format(i)))
        lst.append(v)
    else:
        print(lst)
        for j in lst:
            s=sorted(set(lst))
            print(s)
            print("second largest number:{}".format(s[-2]))


