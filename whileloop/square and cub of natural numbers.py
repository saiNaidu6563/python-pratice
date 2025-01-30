#program for square and cub of first natural numbers
# n =int(input("Enter How Many Natural Nums square and cub ypu want:"))
# if (n<=0):
#     print("{} is invalid input".format(n))
# else:
#     print("Nat Nums\t\tSquares Nat Nums\t\tCubes Nat Nums")
#     i=1
#     s=0
#     ss=0# Called Additive Identity used for accumulaing Sum of Dynamic generated Values
#     cub=0
#     while i<=n:
#         print("\t\t{}\t\t{}\t\t{}".format(i,i**2,i**3))
#         s=s+i
#         ss=ss+i**2
#         cub=cub+i**3
#         i=i+1
#     else:
#         print("*"*50)
#         print("\t\t{}\t\t{}\t\t{}".format(s,ss,cub))
#         print("*"*50)
# process 2:
n=input("Enter How Many Natural Nums square and cub ypu want:")
if n.isdigit():
    num=int(n)
    if num==0:
        print("{} is invalid input".format(num))
    else:
        print("Nat Nums\t\tSquares Nat Nums\t\tCubes Nat Nums")
        i=1
        s=0
        ss=0
        cub=0
        while(i<=num):
            print("\t\t{}\t\t{}\t\t{}".format(i,i**2,i**3))
            s=s+i
            ss=ss+i**2
            cub=cub+i**3
            i=i+1
        else:
            print("*"*50)
            print("\t\t{}\t\t{}\t\t{}".format(s,ss,cub))
            print("*" * 50)