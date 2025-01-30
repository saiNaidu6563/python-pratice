#program for product reverse
n=int(input("enter how much range you want generate:"))
if n<0:
    print("{}is invalid input".format(n))
else:
    p=1
    i=n
    while i>=1:
        print("\t\t{}".format(i))
        p=p*i
        i=i-1
    else:
        print("*"*50)
        print("\t\t fact{}={}".format(n,p))
        print("*" * 50)