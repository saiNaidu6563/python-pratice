#program for generating even numbers within n where n is n positive number
n=int(input("enter how many number u want to generate:"))
if n <=0:
    print("{} is invalid input".format(n))
else:
    print("List of Even Numbers within {}".format(n))
    i=2
    while (i<=n):
        print(i)
        i=i+2
    else:
        print("program completed")