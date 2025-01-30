# try:
#     s1=input("enter val of s1:")
#     s2=input("enter val of s2:")
#     a=int(s1)
#     b=int(s2)
#     c=a/b
# except(ValueError,ZeroDivisionError):
#     print("Don't enter alnum,special symbols:")
#     print("Don't enter zero as den...")
# else:
#     print("-" * 50)
#     print("\ta=",a)
#     print("\tb=",b)
#     print("\tDiv=",c)
#     print("-"*50)
# finally:
#     print("-" * 50)
#     print("Iam from finally block:")
#     print("-"*50)

#procees-2
# try:
# 	print("Program Execution started")
# 	s1=input("\tEnter Value of s1:")
# 	s2=input("\tEnter Value of s2:")
# 	a=int(s1) #----------------------------ValueError
# 	b=int(s2) #----------------------------ValueError
# 	c=a/b  #-------------------------------ZeroDivisionError
# except ZeroDivisionError as z: # Multi Exception Handling Block
# 	print(z)
# except ValueError as v:
# 	print(v)
# else:
# 	print("-------------else block-----------------")
# 	print("\ta=",a)
# 	print("\tb=",b)
# 	print("\tDiv=",c)
# 	print("-------------------------------------------")
# finally:
# 	print("---------------------------------------------")
# 	print("I am from finally block")
# 	print("---------------------------------------------")

#process-3
try:
	print("Program Execution started")
	s1=input("\tEnter Value of s1:")
	s2=input("\tEnter Value of s2:")
	a=int(s1) #----------------------------ValueError
	b=int(s2) #----------------------------ValueError
	c=a/b  #-------------------------------ZeroDivisionError
except ZeroDivisionError : # Multi Exception Handling Block
	print("Don't enter zero as den...")
except ValueError:
	print("Don't Enter alnums,special symbols:")
except SyntaxError:
    print("Don't enter invalid syntax")
except :
    print("oops some thing went wrong:")
else:
	print("-------------else block-----------------")
	print("\ta=",a)
	print("\tb=",b)
	print("\tDiv=",c)
	print("-------------------------------------------")
finally:
	print("---------------------------------------------")
	print("I am from finally block")
	print("---------------------------------------------")