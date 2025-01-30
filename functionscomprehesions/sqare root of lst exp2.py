#program for accepting square root of a given list
lst=[2,4,6,-5,-7,3-9,10]
s=[val**0.5 for val in lst ]
for ov,sv in zip(lst,s):
    if type(sv)!=complex:
        print("\tlist of values and square root values:{}-->{}".format(ov,round(sv,2)))
    else:
        print("\tlist of values and square root values:{}-->{}".format(ov,sv ))
print("-"*80)
#by using set
lst=[2,4,6,-5,-7,3-9,10]
set1={val**0.5 for val in lst }
for ov,sv in zip(lst,set1):
    if type(sv)!=complex:
        print("\tlist of values and square root values:{}-->{}".format(ov,round(sv,2)))
    else:
        print("\tlist of values and square root values:{}-->{}".format(ov,sv    ))