#program for demonstrating global keyword
# #ep1
# def fun1():
#     global a,b #global is a keyword
#     a=a+1
#     b=b+1
# def fun2():
#     global a,b
#     a=a*2
#     b=b*2
# #main program
# a,b=10,20 # Global Variable
# print("Main Program--before fun1():  a={}  b={}".format(a,b))
# fun1() # Function Call
# print("Main Program----after fun1():  a={}  b={}".format(a,b))
# fun2()
# print("Main Program----after fun2():  a={}  b={}".format(a,b))

#ep2
def fun1():
    global a,b #global is a keyword
    a=a+1
    b=b+1
def fun2():
    global a,b
    a=a*2
    b=b*2
def fun3():
    c=a+2 # Here we are Just accessing the val of global var val 'a' but not modifying. so that no need to write global kwd
    d=b+2 # Here we are Just accessing the val of global var val 'b' but not modifying. so that no need to write global kwd
    print("\tc={},d={}".format(c,d))
#main program
a,b=10,20 # Global Variable
print("Main Program--before fun1():  a={}  b={}".format(a,b))
fun1() # Function Call
print("Main Program----after fun1():  a={}  b={}".format(a,b))
fun2()
print("Main Program----after fun2():  a={}  b={}".format(a,b))
fun3()
print("Main Program----after fun3():  a={}  b={}".format(a,b))