#program for course in a order
cr=input("enter a course name:")
if cr== "c".lower():
    print("it is developed by dennis")
if cr=="c++".lower() :
    print("it is developed by Bjarne Stroustrup")
if cr== "python".lower():
    print("it is developed by rosuum ")
if cr=="java".lower():
    print("it is developed by james")
if cr not in "c, c++, python, java".lower():
    print("invalid syntax")