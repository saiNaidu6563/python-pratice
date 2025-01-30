#program for accepting digit and display its name dy using if elif else
# d=float(input("enter the digits:"))
# if d==0:
#     print("{} is zero".format(d))
# elif d==1:
#     print("{} is one".format(d))
# elif d==2:
#     print("{} is two".format(d))
# elif d==3:
#     print("{} is three".format(d))
# elif d==4:
#     print("{} is four".format(d))
# elif d==5:
#     print("{} is five".format(d))
# elif d==6:
#     print("{} is six".format(d))
# elif d==7:
#     print("{} is seven".format(d))
# elif d==8:
#     print("{} is eight".format(d))
# elif d==9:
#     print("{} is nine".format(d))
# elif d>9:
#     print("{} is number".format(d))
# elif d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
#     print("{} is -ve digit".format(d))
# elif d<0 and d not  in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
#     print("{} is -ve number".format(d))

#process 2

# d={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
#    -1:"-one",-2:"-two",-3:"-three",-4:"four",-5:"five",-6:"-six",-7:"-seven",-8:"-eight",-9:"-nine"}
# dig=int(input("enter a digit:"))
# r=d.get(dig) if d.get(dig) !=None else "+ve number" if dig >9 else "-ve number"
# print("{}={}".format(dig,r))

#process 3
d1={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:'eight',9:"nine",
     -1:"-one",-2:"-two",-3:"-three",-4:"four",-5:"five",-6:"-six",-7:"-seven",-8:'eight',-9:"-nine"}
dig=int(input("enter a digit:"))

print("{} is {}".format(dig,d1.get(dig) if d1.get(dig)!=None else "+VE NUMBER" if dig>9 else "-VE NUMBER"))
