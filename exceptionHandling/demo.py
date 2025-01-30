
# try:
#     print("_"*50)
#     s1=input("enter value of s1:")
#     s2=input("enter value of s2:")
#     a=int(s1)
#     b=int(s2)
#     c=a/b
#     print("Div=",c)
#     print("_"*50)
# except ZeroDivisionError:
#     print("don't enter zero as den...")
# except ValueError:
#     print("don't enter alnum and special symbols")
#     print("_"*50)
# finally:
#     print("thx for using")



#process-2
try:
    print("_"*50)
    s1=input("enter value of s1:")
    s2=input("enter value of s2:")
    a=int(s1)
    b=int(s2)
    c=a/b
    print("_"*50)
except ZeroDivisionError:
    print("don't enter zero as den...")
except ValueError:
    print("don't enter alnum and special symbols")
    print("_"*50)
else:
    print("a=",a)
    print("b=",b)
    print("div=",c)
finally:
    print("thx for using")


