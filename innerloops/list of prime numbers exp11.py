#program accepting list of integer values and get prime numbers
# p=int(input("enter list of values you want generate prime numbers:"))
# if p<=0:
#     print("{} is invalid input".format(p))
# else:
#     lst=[]
#     for i in range(1,p+1):
#         lst.append(int(input("enter {} values:".format(i))))
#     else:
#         print("list of values")
#         print(lst)
#         print("-"*50)
#         s=[]
#         for j in lst:
#             if j<=1:
#                 continue
#             r=True
#             for k in range(2,j):
#                 if j%k==0:
#                     r=False
#                     break
#             if r:
#                 s.append(j)
#         print(s)
p=int(input("enter a number:"))
if p<=0:
    print("{} is invalid".format(p))
else:
    lst=[]
    for i in range(1,p+1):
        lst.append(int(input("enter {} value:".format(i))))
    else:
        print("list of values")
        print(lst)
        s=[]
        for j in lst:
            if j<=1:
                continue
            r=True
            for k in range(2,j):
                if j%k==0:
                    r=False
            if r:
                s.append(j)
        print(s)


