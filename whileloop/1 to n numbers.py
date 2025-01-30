#program for generate 1 to n number by using while loop
n=int(input("enter a number:"))
if n<=0:
    print("invalid input")

else:
    i=1
    while(i<=n):
        print(i)
        i=i+1
    else:
        print("i am from else part of while loop")
    print("while loop excecution Over")
print("I am from if...else stmt")
