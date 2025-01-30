#Python program to print even numbers in a list
n=int(input("enter numbers which you want:"))
if n<=0:
    print("{} is invalid input".format(n))
else:
    s=[]
    for i in range(1,n+1):
            val=float(input("enter {} values:".format(i)))
            s.append(val)
    else:
        print(s)
        l=[]
        print("*" * 50)
        for v in s:
            if v%2==0:
                l.append(v)
        else:
            print("even number{}".format(l))