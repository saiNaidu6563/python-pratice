#program generating prime number within given range
n=int(input("enter a number u want generate prime numbers:"))
if n<=1:
    print("{} is invalid input".format(n))
else:
    print("-----------------------------------")
    print("List of Prime Numbers")
    print("-----------------------------------")
    nop=0
    for i in range(2,n+1):
        res = True
        for j in range(2,i) :
            if i%j==0:
                res=False
                break
        if res:
            print("\t\t {}".format(i))
            nop=nop+1
    else:
         print("number of prime within {}={}".format(n,nop))
