#program for accepting line of text and get those words first and last letters are same
def flletters(n):
    if len(n)==0:
        print("please enter words -->try again")
    elif n.isspace():
        print("don't enter space-->try again")
    elif  n.isdigit():
        print("don't enter numbers")
    else:
        w=n.split()
        for v in w:
            if v[0]==v[-1]:
                print("{}----- is same words".format(v))
            else:
                print("{}----- is not same words".format(v))



#mainprogram
n=input("enter the line of text:")
flletters(n)