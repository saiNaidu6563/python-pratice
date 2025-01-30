#program for accepting number and decide whether it is perfect number or not
def perfect(n):
    if n<=1:
        print("{} is invalid input".format(n))
    else:
        print("factorial number{}".format(n))
        lst=[]
        for i in range(1,(n//2)+1):
            if n%i == 0:
                lst.append(i)
        else:
            print("factors of {} :{}".format(n, lst))
            print("perfect number")
            p = 0
            p=sum(lst)
            if p==n:
                print("{} is perfect number".format(n))
            else:
                print("{} is not perfect number".format(n))


#main program
n=int(input("enter a number:"))
perfect(n)