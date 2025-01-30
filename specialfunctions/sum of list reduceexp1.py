#program for accepting sum of list
# import functools
#
# lst=list(map(float,input("enter list of values separated by space:").split()))
# print("given values=",lst)
# s=functools.reduce(lambda k,v:k+v,lst)
# print(s)

import functools
def sumop(k,v):
    return k+v

lst=list(map(float,input("enter list of values separated by space:").split()))
print("given values=",lst)
s=functools.reduce(sumop,lst)
print(s)