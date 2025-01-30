#program for accepting numerical values and find +ve and -ve values in a separate list
s=[2,4,5,6,-1,-3,-7,-6,8,-9,7,9]
print("list of values=",s)
print('-'*50)
s1=[val for val in s if val>0]
print("positive values{}".format(s1))
s2=[val for val in s if val<0]
print("negative values:{}".format(s2))

print("==============by using set comprehesion===========")
s=[2,4,5,6,-1,-3,-7,-6,8,-9,7,9]
print("list of values=",s)
print('-'*50)
set1={val for val in s if val>0}
print("positive values{}".format(set1))
set2={val for val in s if val<0}
print("negative values:{}".format(set2))