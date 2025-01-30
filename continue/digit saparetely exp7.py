#program for accepting line of text and get digit and separate spacial symbol
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
           if not i.isalpha():
               ap.append(i)
       else:
           print("".join(ap))
           print("* "*50)
           ds=[]
           for v in ap:
               if  v.isdigit() :
                   ds.append(v)
           else:
               print("given numbers")
               print("".join(ds))
               print("*"*50)
               ss = []
               for v in ap:
                   if not v.isdigit():
                       ss.append(v)
               else:
                   print("given special symbols")
                   print("".join(ss))



