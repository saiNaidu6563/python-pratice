#program for accept which will print the words from anyfile whose length range blw 4&5
try:
    f=input("enter a file name:")
    with open(f,"r") as rp:
        r=rp.read()
        w=r.split()

        for i in w:
            #if len(i) in [4 and 5]:
            if 4<=len(i)<=5:
                print(i)

except FileNotFoundError:
    print("file not there")
