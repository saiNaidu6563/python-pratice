#logic no :5
#This Program works for Swappping of Numerical Values
a,b=int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print("Original Value of a={}".format(a))
print("Original Value of b={}".format(b))
print("*"*50)
a=a^b
b=a^b
a=a^b
print("Swapped Value of a={}".format(a))
print("Swapped Value of b={}".format(b))
print("*"*50)
