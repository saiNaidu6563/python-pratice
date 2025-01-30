#program for accepting biggest and smallest of list
# import functools
# lst=list(map(float,input("enter list of values separated by space:").split()))
# print("given values=",lst)
# bv=functools.reduce(lambda k,v:k if k>v else v,lst)
# sv=functools.reduce(lambda k,v:k if k<v else v,lst)
# print("biggest({})=",bv)
# print("smallest({})=",sv)

# import functools
# def big(k,v):
#     if k>v:
#         return k
#     else:
#         return v
# def small(k,v):
#     if k<v:
#         return k
#     else:
#         return v
#
# lst=list(map(float,input("enter list of values separated by space:").split()))
# print("given values=",lst)
# bv=functools.reduce(big,lst)
# sv=functools.reduce(small,lst)
# print("biggest({})=",bv)
# print("smallest({})=",sv)


import functools
def big(k,v):
    return k if k>v else v
def small(k,v):
    return k if k<v else v

lst=list(map(float,input("enter list of values separated by space:").split()))
print("given values=",lst)
bv=functools.reduce(big,lst)
sv=functools.reduce(small,lst)
print("biggest({})=",bv)
print("smallest({})=",sv)
