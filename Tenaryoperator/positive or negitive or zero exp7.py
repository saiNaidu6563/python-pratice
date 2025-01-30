#write the code which will accept numerical values and decide when it is positive or negative or zero
a= int(input("enter the val of a:"))
pnz="positive" if a>0 else "negative" if a<0 else "zero"
print("{}={}".format(a,pnz))