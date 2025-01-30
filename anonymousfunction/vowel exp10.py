#program for accepting word and decide whether it is vowel are not
w=lambda  a:"vowel" if any(v in list("aeiou") for v in a )else "not vowel"
a=input("enter a word:")
r=w(a)
print(r)