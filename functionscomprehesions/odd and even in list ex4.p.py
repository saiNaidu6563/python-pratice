#program for accepting even and odd in  a given list
s=[2,3,4,5,6,7,8,9,1,10,11]
lst1=[v for v in s if v%2==0]
print("even of a list:{}".format(lst1))
lst2=[val for val in s if val%2!=0]
print("0dd of a list:{}".format(lst2))
print("=========by using set===========")
s=[2,3,4,5,6,7,8,9,1,10,11]
set1=[v for v in s if v%2==0]
print("even of a list:{}".format(set1))
set2=[val for val in s if val%2!=0]
print("0dd of a list:{}".format(set2))

