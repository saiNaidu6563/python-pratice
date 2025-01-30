#logic no :3
#This Program works for Swappping of Numerical Values
a,b=float(input("enter the val of a:")),float(input("enter the val of b:"))
print("original val of a={}".format(a))
print("original val of b:".format(b))
print("*"*50)
#logic no:3
a=a+b
b=a-b
a=a-b
print("\t\t swaped val of a ={}".format(a))
print("\t\t swaped val of b = {}".format(b))
print("*"*50)