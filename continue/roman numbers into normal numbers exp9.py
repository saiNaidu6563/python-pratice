#program for accepting convert roman numbers into normal numbers
rm={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
n=input("Enter a Roman numeral you want to convert to a normal number: ")
if len(n)==0:
    print("invalid input:{}".format(n))
else:
    if n.islower():
        print("{} is Invalid input".format(n))
    else:
        nv=0
        for i in range(len(n)):
            cv=rm.get(n[i],0)
            if i+1<len(n):
                if(n[i]=="I" and n[i+1] in "VX") or (n[i]=="X" and n[i+1] in "LC") or(n[i]=="C" and n[i+1] in "DM"):
                    nv=nv-cv
                else:
                    nv=nv+cv
            else:
                nv=nv+cv
        print("{} has the value: {}".format(n.upper(), nv))