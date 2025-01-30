#Python program to find largest number in a list
s=int(input("enter a list of number:"))
if s<=0:
    print("invalid input:")
else:

    lst=[]
    for i in range(1,s+1):
        lst.append((input("enter {} value:".format(i))))
        print(lst)
    else:
        print(max(lst))
