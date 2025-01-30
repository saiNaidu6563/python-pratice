#program for factorial of given positive number
f=int(input("enter how much range of factorial number you want:"))
if(f<0):
    print("{} is a invalid input".format(f))
else:
    print("natural numbers within{}".format(f))
    p=1
    i=1
    while(i<=f):
        # print("\t\t{}".format(i))
        p=p*i
        i=i+1
    else:
        print("*"*50)
        print("\t\t factorial{}={}".format(f,p))
        print("*"*50)

