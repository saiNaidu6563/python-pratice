#write the code which will accept a numerical integer whether it is even or odd

a=int(input("enter the vales :"))
ed= "even"if a%2==0 else "odd"
print("{}={}".format(a,ed))

# a=int(input("enter the vales :"))
# ed= "even"if a%2==0 else "odd"
# ed="{} is Invalid Input".format(a) if a<=0 else "{} Even".format(a) if a%2==0 else "{} is Odd".format(a)
# print("ed")