#Python program to interchange first and last elements in a list
s= int(input("enter a number:"))
if s<=0:
    print("{} is invalid input".format(s))
else:
    lst=[]
    for v in range(1,s+1):

        val=int(input("enter {} value:".format(v)))
        lst.append(val)
        # print(lst)
    else:
        print("*"*50)
        lst[0], lst[-1] = lst[-1], lst[0]
        print(lst)
