#program for accepting list consonents:
w=int(input("enter a list of words you want generate:"))
if w<=0:
    print("{} is invalid input".format(w))
else:
        lst=[]
        for i in range(1,w+1):
            lst.append(input("enter {} value:".format(i)))
        else:
            print("list of words")
            print(lst)
            print("*"*50)
            s=[]
            for j in lst:
                r=True
                for k in j:
                    if k.lower()  in list("aeiou"):
                        r=False
                        break
                if r:
                    s.append(j)
            print(s)