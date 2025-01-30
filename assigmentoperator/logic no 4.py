#logic no :4
#This Program works for Swappping of Numerical Values
a,b=float(input("Enter Value of a:")),float(input("Enter Value of b:"))
print("Original Value of a={}".format(a))
print("Original Value of b={}".format(b))
print("*"*50)
#Swapping Logic 4
a=a*b
b=a//b
a=a//b
print("Swapped Value of a={}".format(a))
print("Swapped Value of b={}".format(b))
print("*"*50)



