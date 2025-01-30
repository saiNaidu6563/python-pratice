#Python | Ways to find length of list
s=int(input("enter a list of number:"))
if s<=0:
    print("invalid input:")
else:
    lst=[]
    c=0
    for i in range(1,s+1):
        lst.append(float(input("enter {} value:".format(i))))
        print(lst)
        c=c+i
    else:
        print("*"*50)
        print(len(lst))
        print(max(lst))
        print(min(lst))
        print(c)
