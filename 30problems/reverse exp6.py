#Python | Reversing a List
s=int(input("enter a list of number:"))
if s<=0:
    print("invalid input:")
else:

    lst=[]
    for i in range(1,s+1):
        lst.append((input("enter {} value:".format(i))))
        print(lst)
    else:
        print("*" * 50)
        lst.reverse()
        print(lst)
        # print("*"*50)
        print(lst[::-1])
        lst.sort()
        print(lst)
        lst.sort(reverse=True)
        print(lst)
