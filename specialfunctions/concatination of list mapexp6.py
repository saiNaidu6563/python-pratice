#program for accepting two list of words and find their concatination
lst1=list(map(str,input("enter first list of words separated by space:").split()))
lst2=list(map(str,input("enter second list of words separated by space:").split()))
if len(lst1)>len(lst2):
    for i in range(len(lst1)-len(lst2)):
        lst2.append("unknown")
elif len(lst1)<len(lst2):
    for i in range(len(lst2)-len(lst1)):
        lst1.append("unknown")
lst3=list(map(lambda a,b:a.isalpha() and b.isalpha()and a+b,lst1,lst2))
print("*"*50)
print("\tlst2\t\t\tlst2\t\t\tlst3")
print("*"*50)
for k,v,u in zip(lst1,lst2,lst3):
    print("\t{}\t\t\t{}\t\t{}".format(k,v,u))
print("*"*50)
