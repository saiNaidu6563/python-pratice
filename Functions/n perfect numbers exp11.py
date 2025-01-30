#program for accepting n factorial perfect numbers
def perfect_number(n):
    if n<=0:
        print("{}is in valid input".format(n))
    else:
        c=0
        n1=1
        while c<n:
            s=0
            for i in range(1,n1):
                if n1%i==0:
                    s=s+i
            if s==n1:
                print("it is perfect number{}".format(n1))
                c=c+1
            n1=n1+1
#main program
n=int(input("enter value of n:"))
perfect_number(n)