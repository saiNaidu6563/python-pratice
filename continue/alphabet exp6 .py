#program for accepting line of text and get only alphabets
a=input("enter a line of text:")
if a==0:
    print("please enter words-->try again")
else:
   if a.isspace():
       print("Don't enter space")
   else:
       print("*" * 50)
       ap = []
       for i in a:
           if i.isalpha():
               ap.append(i)
       else:
           print("".join(ap))






