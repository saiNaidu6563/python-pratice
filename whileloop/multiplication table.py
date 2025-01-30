#program for multiplication table for given positive number
# n=int(input("enter a number for multiplication table:"))
# if n<=0:
#     print("{} is invalid input".format(n))
# else:
#     i=1
#     while(i<=10):
#         print("{}x{}={}".format(n,i,n*i))
#         i=i+1
#         else:
#             print("program completd")
# else:
#     print("invalid input {}:".format(n))

#process 2:
n =input("Enter a Number for Generating Mul Table:")
if(n.isdigit()):
    n=int(n)
    if n==0:
        print("{} is invalid input".format(n))
    else:
        i=1
        while(i<=10):
            print("{}x{}={}".format(n,i,n*i))
            i=i+1
        else:
            print("program completd")
else:
    print("invalid input {}:".format(n))