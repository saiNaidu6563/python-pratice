#program for accepting to find square and square root of element in list by using dict
s=[2,4,5,6,78,8]
d={val:val**2 for val in s}
print("square values:{}".format(d))
d1={v:v**0.5 for v in s}
print("square root values:{}".format(d))
for k,v in d.items():
    print("{}-->{}".format(k,v))
print('-'*50)
for k,v in d1.items():
    print("{}-->{}".format(k,v))

print('='*80)
lst=[2,14,16,9,3,15,25,81]
sqrd={val:val**2 for val in lst} # Dict Comprehension
print("---------------------------------------")
print("Given Value\t\tSquare")
print("---------------------------------------")
for v,sv in sqrd.items():
    print("\t{}\t\t\t{}".format(v, sv))
print("---------------------------------------")
sqrtd={val:val**0.5 for val in lst} # Dict Comprehension
print("---------------------------------------")
print("Given Value\t\tSquareRoot")
print("---------------------------------------")
for v,sv in sqrtd.items():
    print("\t{}\t\t\t{}".format(v, round(sv,2)))
print("---------------------------------------")

