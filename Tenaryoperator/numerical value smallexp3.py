#write the code which will accept two numerical values and find the smallest values and check for equality

# a,b=float(input("enter the val of a:")),float(input("enter the val of b:"))
# small= a if a<b else b if b<a  else "both are equal "
# print("smallest {},{}={}".format(a,b,small))

while(True):
    try:
        a, b = float(input("enter the val of a:")), float(input("enter the val of b:"))
        small = a if a < b else b if b < a else "both are equal "
        print("smallest {},{}={}".format(a, b, small))
        break
    except ValueError:
        print("don't write symbols write only numerical values ")