#program generating prime number within given range
# n=int(input("Enter the How many Range values primes will de displayed:"))
# if(n<=1):
#     print("Invalid input")
# else:
#     print("The first {} prime numbers are".format(n))
#     prime=0
#     num=2
#     while prime <n:
#         res=True
#         for i in range(2,int(num ** 0.5) + 1):
#             if num%i==0:
#                 res=False
#                 break
#         if res:
#             print(num)
#             prime +=1
#         num +=1
# print("-"*50)
#

n=int(input("Enter the How many Range values primes will de displayed:"))
if(n<=1):
    print("Invalid input")
else:
    print("The first {} prime numbers are".format(n))
    prime=0
    num=2
    while prime<n:
        r=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                r=False
                break
        if r:
            print(num)
            prime+=1
        num+=1