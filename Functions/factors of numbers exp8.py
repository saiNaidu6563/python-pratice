#program accepting factors of a given numbers by using functions
def factornum(a):

    if a<=1:
        print("{} is invalid input".format(a))
    else:
        for i in range(1,(a//2)+1):
            if a%i==0:
                print ("\t{}".format(i))

#main program
a=int(input("enter a number which will find factorial of number:"))
r=factornum(a)
