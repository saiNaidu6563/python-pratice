#program for accepting list of values and obtain only positive values
# def pos(val):
#     if val >0:
#         return True
#     else:
#         return False
# #mainprogram
# print("enter a list of values separated space:")
# lst=[float(v) for v in input().split()]
# plst=list(filter(pos,lst))
# print(plst)

#by using anonymous function
# pos=lambda val:val>0
# #mainprogram
# print("enter a list of values separated space:")
# lst=[float(v) for v in input().split()]
# plst=list(filter(pos,lst))
# print(plst)

#process-2
print("enter a list of values separated space:")
lst=[float(v) for v in input().split()]
plst=list(filter(lambda val:val>0,lst))
print(plst)


