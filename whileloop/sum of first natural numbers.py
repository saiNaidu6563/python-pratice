#program for compute sum of first n natural number
# n=input("enter how much range you want generate natural numbers: ")
# if(n.isdigit()):
#     num=int(n)
#     if num==0:
#         print("{} is invalid input".format(num))
#     else:
#         i=1
#         s=0
#         while(i<=num):
#             print(i)
#             s=s+i
#             i=i+1
#         else:
#             print("-" * 50)
#             print("Sum={}".format(s))
#             print("-" * 50)

#process 2:
n =int(input("Enter How Many Natural Nums Sum u want:"))
if (n<=0):
    print("{} is invalid input".format(n))
else:
    print("Natural Numbers within:{}".format(n))
    i=1
    s=0# Called Additive Identity used for accumulaing Sum of Dynamic generated Values
    while i<=n:
        print(i)
        s=s+i
        i=i+1
    else:
        print("*"*50)
        print("sum ={}".format(s))
        print("*"*50)

