def simpleint():
    p=float(input("enter principle amt:"))
    t=float(input("enter time:"))
    r=float(input("enter rate of interest:"))
    si=(p*t*r)/100
    t=p+si
    print("*"*50)
    print("principle amt:{}".format(p))
    print("time:{}".format(t))
    print("rate of interest:{}".format(r))
    print("simple interest:{}".format(si))
    print("total amt:{}".format(t))