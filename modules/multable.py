def table(n):
    if n<=0:
        print("{} is invalid input".format(n))
    else:
        print("-"*50)
        print("table for :{}".format(n))
        print("_"*50)
        for i in range(1,11):
            print("\t{}x{}={}".format(n,i,i*n))
        print("*"*50)