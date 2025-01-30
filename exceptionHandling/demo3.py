# try:
# 	print("Program Execution started")
# 	s1=input("\tEnter Value of s1:")
# 	s2=input("\tEnter Value of s2:")
# 	a=int(s1) #----------------------------ValueError
# 	b=int(s2) #----------------------------ValueError
# 	c=a/b  #-------------------------------ZeroDivisionErro
#  # Multi Exception Handling Block
# except Exception:
# 	print("oops some thig went wrong")
# else:
# 	print("-------------else block-----------------")
# 	print("\ta=",a)
# 	print("\tb=",b)
# 	print("\tDiv=",c)3
#
# 	print("-------------------------------------------")
# finally:
# 	print("---------------------------------------------")
# 	print("I am from finally block")
# 	print("---------------------------------------------")


#process-2
# try:
# 	print("Program Execution started")
# 	s1=input("\tEnter Value of s1:")
# 	s2=input("\tEnter Value of s2:")
# 	a=int(s1) #----------------------------ValueError
# 	b=int(s2) #----------------------------ValueError
# 	c=a/b  #-------------------------------ZeroDivisionError
# except BaseException:
# 	print("some thing wrong")
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



#only defalut exception
try:
	print("Program Execution started")
	s1=input("\tEnter Value of s1:")
	s2=input("\tEnter Value of s2:")
	a=int(s1) #----------------------------ValueError
	b=int(s2) #----------------------------ValueError
	c=a/b  #-------------------------------ZeroDivisionError

except :
	print("wrong")
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