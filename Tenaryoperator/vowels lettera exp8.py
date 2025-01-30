#write the code which will accept letters and decide whether it is vowels or consonents
# a=input("enter the letters:")
# v= "vowels " if a in  ("a","e","i","o","u","A","E","I","O","U") else "not vowels"
# print(f"vowels of {a}={v}")
# a=input("enter the letters:")
# v= "not vowels " if a in  list("aeiouAEIOU") else "vowels"
# print(f"vowels of {a}={v}")

a=input("enter the letters:")
v=  "  vowels " if a in  list("aeiou AEIOU") else " no vowels"
print(f"vowels of {a}={v}")

