#write the code which will accept a words from keyboard and decide whether it is vowels are not

a=input("enter the words from keyboard:")
vo="vowels" if any(char in "aeiouAEIOU" for char in a) else "Not vowels"

print(f"vowel word {a}={vo}")