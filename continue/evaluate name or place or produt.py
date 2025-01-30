#pragram for accepting evalute name or place or product
n=input("enter a name:")
print("given name:{}".format(n))
w=n.split()
nv=True
for v in w:
    if not v.isalpha():
        nv=False
        break
if nv:
    print("{} is valid name".format(n))
else:
        print("{} is invalid name".format(n))