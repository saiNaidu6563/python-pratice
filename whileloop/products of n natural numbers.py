#program for which will find product of n natural numbers
n=int(input("enter how many range u want numbers:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("natural numbers within{}".format(n))
    i=1
    p=1
    while(i<=n):
        print(i)
        p = p * i
        i = i + 1
    else:
        print("*"*50)
        print("product={}".format(p))
        print("*"*50)
