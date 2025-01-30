#write a code which will accept value and decide whether  it is palindrome are not
val=input("enter the value :")
if val==val[::-1]:
    print("{} is palindrome".format(val))
if val!=val[::-1]:
    print("{} is not palindrome".format(val))