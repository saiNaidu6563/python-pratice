#program for accepting line of text from list of words
# import functools
# lst=list(map(str,input("enter list of words separated by comma:").split(",")))
# print("given values=",lst)
# s=functools.reduce(lambda k,v:k+" "+v,lst)
# print(s)

import functools
def sai(k,v):
    return k+" "+v
lst=list(map(str,input("enter list of words separated by comma:").split(",")))
print("given values=",lst)
s=functools.reduce(sai,lst)
print(s)

