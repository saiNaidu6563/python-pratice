#program for accepting number whether it is decided prime are not

# s=int(input("enter a number:"))
# if s<=1:
#     print("{} is invalid input".format(s))
# else:
#     res = "prime"
#     for v in range(2,s):
#         if s%v==0 :
#             res="not prime"
#             break
#     print("{}={}".format(s,res))

#process -2
s=int(input("enter a number:"))
if s<=1:
    print("{} is invalid input".format(s) )
else:
    prime=True
    for v in range(2,s):
        if s%v==0 :
            prime=False
            break
    print("{} is PRIME".format(s) if prime else "{} is NOT PRIME".format(s))

