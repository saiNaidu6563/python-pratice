#program for accepting perfect numbers within 10000
def perfect(n):
    for i in range(1,n+1):
        p=0
        for j in range(1,(i//2)+1):
            if i%j==0:
                p=p+j
        else:
           if(p==i):
                print("perfect numbers {}".format(i))

#main program
perfect(1000)