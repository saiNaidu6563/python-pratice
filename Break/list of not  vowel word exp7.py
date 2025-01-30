#program for accepting list of words and get those words which are not vowel


word=int(input("enter a list of not vowel words you want:"))
if word<=0:
    print("{} is invalid input".format(word))

else:
    lst=[]
    for w in range(1,word+1):
        lst.append(input("enter {} word:".format(w)))
    else:
        print(lst)
        print("*"*50)
        vlst=list()
        vowels="aeiou"
        for v in lst:
            if not any(char in vowels for char in v.lower()):
                vlst.append(v)

        if vlst:
            print("{} not vowel".format(vlst))
        else:
            print("vowel")


