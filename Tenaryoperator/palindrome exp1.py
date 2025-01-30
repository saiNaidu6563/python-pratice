#write a code which will accept and decide whether palindrome are not
#palindrome means original value is equal to reverse value

# value=input("enter the value :")
# res="palindrome" if value==value[::-1] else "not palindrome"
# print("{} ={}".format(value,res))
a=input("enter the value :")
res="palindrome" if a==a[::-1] else "not palindrome"
print("{} ={}".format(a,res))