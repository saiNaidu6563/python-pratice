#program for natural numbers n to 1 where n is positive
# n=input("Enter a number which u want generate number:")
# if n.isdigit():
#     num=int(n)
#     if num ==0:
#         print("invalid input{}".format(num))
#     else:
#         i=num
#         while(i>=1):
#             print(i)
#             i=i-1
#         else:
#             print("completed")
# else:
#     print("invalid input")

#process 2

n=int(input("enter a number"))
if n<=0:
    print("invalid input{}".format(n))
else:
    i=n
    while i>=1:
        print(i)
        i=i-1
    else:
        print("program completed")
