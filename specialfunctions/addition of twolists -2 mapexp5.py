#program for accepting addition  two lists with equal lists
print("enter first list values separated by space:")
lst1=list(map(float,input().split()))
print("enter second list values separated by space:")
lst2=list(map(float,input().split()))
if len(lst1)>len(lst2):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(0)
elif len(lst1)<len(lst2):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0)
sum=list(map(lambda a,b:a+b,lst1,lst2))
print("*"*50)
print("given lst1\t\tgiven lst2\t\tsum of values:")
print("*"*50)
for l1,l2,s  in zip(lst1,lst2,sum):
    print("\t{}\t\t\t\t{}\t\t\t\t{}".format(l1,l2,s))
print("*"*50)
