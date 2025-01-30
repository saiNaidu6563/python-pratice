#Python | Multiply all numbers in the list
s= int(input("enter a number:"))
if s<=0:
    print("{} is invalid input".format(s))
else:
    lst=[]
    m=1
    for v in range(1,s+1):
        val=int(input("enter {} value:".format(v)))
        lst.append(val)
        m=m*val
        # print(lst)
    else:
        print("multiple of {}={}".format(lst,m))
