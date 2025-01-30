#program for generating odd numbers in reverse order within n
n=int(input("enter how many range in which  you want odd numbers:"))
if (n<=0):
    print("{} is invalid input".format(n))
else:
    print("*" * 50)
    print("List of odd Numbers within {}".format(n))
    if n % 2 == 0:  # If n is odd, start from n-1
        n = n - 1
    i = n
    while (i >= 1):
        print(i)
        i=i-2
    else:
        print("program completed")
        print("*" * 50)

