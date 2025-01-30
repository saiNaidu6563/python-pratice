#program for accepting words whether it is palindrome are not
# w=int(input("enter a words you want:"))
# if w<=0:
#     print("please enter words-->try again")
# else:
#     lst=[]
#     for v in range(1,w+1) :
#         lst.append(input("enter {} value:".format(v)))
#     else:
#         print(lst)
#         plst=list()
#         for v in lst:
#             # if v==v[::-1]:
#                 plst.append("palindrome"if v==v[::-1] else "not palindrome")
#
#         # print("{} is palindrome".format(v) if plst else "{} is not palindrome".format(v))
#
#         else:
#             print("*"*50)
#             print("\t{} is {}".format(lst,plst))
#


#process-2
w=int(input("enter a words you want:"))
if w<=0:
    print("please enter words-->try again")
else:
    lst=[]
    for v in range(1,w+1) :
        lst.append(input("enter {} value:".format(v)))
    else:
        print(lst)
        print("*"*50)
        plst=list()
        for v in lst:
            if v==v[::-1]:
                plst.append(v)
        if plst:
            print("{} is palindrome".format(plst))
        else:
            print("not palindrome")





