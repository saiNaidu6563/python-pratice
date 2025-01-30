#Python program to find N largest elements from a list
from heapq import nlargest

s=int(input("enter a list of number:"))
if s<=0:
    print("invalid input:")
else:
    lst=[]
    for i in range(1,s+1):
        lst.append((input("enter {} value:".format(i))))
    else:
        print(lst)
        n=int(input("enter the no  largest elements to find: "))
        if n<=0 or n>len(lst):
            print("invalid input:{}".format(n))
        else:
            lst.sort(reverse=True)
            nlarg=lst[:n]
            print(f"The {n} largest elements are: {nlarg}")
