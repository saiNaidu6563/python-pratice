#program for accepting list of numerical integers values and generate their tables
n=int(input("enter list of numbers you want generate numbers:" ))
if n<=0:
    print("{}is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        lst.append(int(input("enter a {} values:".format(i))))
    else:
        print("List of Values")
        print(lst)
        print("*"*50)
        for j in lst:
            if n<=0:pass
            else:
                print("Mul Table for :{}".format(j))
                for k in range(1,11):
                    print("\t\t{} x {} ={}".format(j,k,j*k))

