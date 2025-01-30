#program for accepting print key as value and value as key
d={10:"Python",20:"C",30:"Java",40:"Django",50:'CPP'}
print(d)
print("_"*50)
rd={v:k for k,v in d.items()}
print(rd)
print("*"*80)
r={}
for k in d:
    #r[d.get(k)]=k
    r[d[k]]=k
    print(r)