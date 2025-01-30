#write code which will accept two numerical values and find biggest and equality

a,b=float(input("enter the val of a:")),float(input("enter the val of b:"))
big= a if a>b else b  if b>a else "all are equal"
print("biggest (a={},b={})={}".format(a,b,big))