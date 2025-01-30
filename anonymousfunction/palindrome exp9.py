#program for accepting word and decide whether it is palindrome are not
w=lambda wr: "palindrome" if wr==wr[::-1] else "not palindrome"
wr=input("enter a word:")
r=w(wr)
print(r)