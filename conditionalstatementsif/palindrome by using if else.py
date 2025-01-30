#program for  value whether it is palindrome are not by using if else
p=input("enter a  value:")
if p==p[::-1]:
    print("{} is palindrome".format(p))
else:
    print("{} is not palindrome".format(p))