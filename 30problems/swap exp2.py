#Python program to swap two elements in a list
s=int(input("enter a list of number:"))
if s<=0:
    print("invalid input:")
else:
    lst=[]
    for i in range(1,s+1):
        lst.append(float(input("enter {} value:".format(i))))
        print(lst)
    else:
        print("*"*50)
        lst[2],lst[3]=lst[3],lst[2]
        print(lst)
