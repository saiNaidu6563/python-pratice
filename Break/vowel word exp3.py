#program for accepting a word whether it is vowel are not
v=input("enter a word:")
if len(v)==0:
    print("please enter words-->try again")
else:
    if v.isspace():
        print("don't enter space-->try again")
    else:
        r="not vowel"
        for i in v:
            if i in list("aeiou"):
                r=" vowel"
                break
        print("{} is{}".format(v,r))