#Python program to find smallest number in a list
s=int(input("enter a list of number:"))
if s<=0:
    print("invalid input:")
else:
    lst=[]
    for i in range(1,s+1):
        lst.append((input("enter {} value:".format(i))))
    else:
        print(min(lst))
        s=sorted(set(lst))
        print("smallest numbers:{}".format(s[0]))
