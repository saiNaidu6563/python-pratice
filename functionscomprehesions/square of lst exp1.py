#programm for accepting square of for every element in list
s=int(input("enter a list of values:"))
if s<=1:
    print("invalid input")
else:
    s1=[val**2 for val in range(2,s+1) ]
    print(s1)
print("===========process-2=============")
lst=[2,4,6,0,-3,-8,9]
lst1=[v**2 for v in lst]
print("square of a list:{}".format(lst1))
for i,j in zip(lst,lst1):
    print("{}-->{}".format(i,j))
print("-"*80)
#by using set
lst=[2,4,6,0,-3,-8,9]
set1={v**2 for v in lst}
print("square of a list:{}".format(set1))



