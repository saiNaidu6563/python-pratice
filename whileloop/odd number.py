#program for  generating odd numbers  within n numbers where n is positive number
n=int(input("enter how many range in which  you want odd numbers:"))
if (n<=0):
    print("{} is invalid input".format(n))
else:
    print("*" * 50)
    print("List of odd Numbers within {}".format(n))
    i=1
    while (i<=n):
        print(i)
        i=i+2
    else:
        print("program completed")
        print("*"*50)