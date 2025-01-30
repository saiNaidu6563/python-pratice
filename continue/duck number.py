#program for accepting numerical values into Duck number
n=input("enter a number:")
if n[0]=="0":
    print("{} is not duck number".format(n))
else:
    s="not duck"
    for v in (n):
        if v=="0":
            s="duck"
            break

    print("{} is {}".format(n,s))

