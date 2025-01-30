#write a python code which will accept a  any digit and display the name of digits by using if else
n=int(input("enter the digit:"))
if n==0:
    print("{} is zero ".format(n))
else:
    if n==1:
        print("{} is one".format(n))
    else:
        if n==2:
            print("{} is two".format(n))
        else:
            if n==3:
                print("{} is three".format(n))
            else:
                if n==4:
                    print("{} is four".format(n))
                else:
                    if n==5:
                        print("{} is five".format(n))
                    else:
                        if n==6:
                            print("{} is six".format(n))
                        else:
                            if n==7:
                                print("{} is seven".format(n))
                            else:
                                if n==8:
                                    print("{} is eight".format(n))
                                else:
                                    if n==9:
                                        print("{} is nine".format(n))
                                    else:
                                        if n>9:
                                            print("{} is number".format(n))
                                        else:
                                            if n in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
                                                print("{} is - ve digit".format(n))
                                            else:
                                                print("{} is -ve number".format(n))


