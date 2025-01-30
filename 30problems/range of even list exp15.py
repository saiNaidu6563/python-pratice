#Python program to print all even numbers in a range
n=int(input("enter numbers which you want:"))
if n<=0:
    print("{} is invalid input".format(n))
else:
    for i in range(1,n+1):
        if i%2==0:
            print(i)