#program for generating 1to n numbers multiplication tables
n=int(input("enter number how many tables u want:"))
if n<=0:
    print("{} is invalid input".format(n))
else:
    for i in range(1,n+1):
        print(i)
        print("*"*50)
        for j in range(1,21):
            print("\t\t{}x{}={}".format(i,j,i*j))
        else:
            print("*"*50)