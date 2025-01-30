#program for  accept count no of lines,words,charaters ina file
fc=input("enter a file name:")
nl,nw,nc=0,0,0
with open(fc,"r") as rp:
    r=rp.readlines()
    for i in r:
        nl=nl+1
        nw=nw+len(i.split())
    else:
        print("=" * 50)
        print("Number of Lines=", nl)
        print("Number of Words=", nw)
        print("Number Chars=", nc)
        print("=" * 50)