#program for accepting line of text and separate even word length and odd word separate
w=input("enter a line of text:")
wr=w.split()
print(wr)
d={v:len(v) for v in wr if len(v)%2==0 }
print("even words:{}".format(d))
d1={v:len(v) for v in wr if len(v)%2!=0 }
print("even words:{}".format(d1))
for k,v in d.items():
    print("{}---.{}".format(k,v))
print("_"*50)
for k,v in d1.items():
    print("{}-->{}".format(k,v))