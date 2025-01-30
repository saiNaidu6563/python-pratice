#Python program to find sum of elements in list
s= int(input("enter a number:"))
if s<=0:
    print("{} is invalid input".format(s))
else:
    lst=[]
    st=0
    for v in range(1,s+1):
        val=float(input("enter {} value:".format(v)))
        lst.append(val)
        st=st+val
    else:
        print("sum of {}={}".format(lst,st))

