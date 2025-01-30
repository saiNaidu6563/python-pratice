#program for  accepting line of text and get of even word length and odd word length
def evenodd(n):
    if n==0:
        print("please enter words -->try again")
    elif n.isspace():
        print("don't enter space")
    else:
        w=n.split()
        ed={}
        od={}
        for v in w:
            if len(v)%2==0:
                ed[v]=len(v)
            else:
                od[v]=len(v)
        else:
            print("Even words and their Length")
            for e,o in ed.items():
                print("{}-->{}".format(e,o))
            print("=" * 50)
            print("Odd words and their Length")
            for e,o in od.items():
                print("{}--->{}".format(e,o))
            print("="*50)
            for wl in ed.items():
                print("{}--->{}".format(wl[0],w[1]))
            print("*"*50)
            for x in od.keys():
                print("{}-->{}".format(x,od.get(x)))


#main program
n=input("enter line of text:")
evenodd(n)