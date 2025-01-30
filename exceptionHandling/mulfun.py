from mulexception import NegativeError,ZeroError
def table(n):
    if n<=-1:
        raise NegativeError
    elif n==0:
        raise ZeroError
    else:
        for i in range(1,21):
            print("\t\t{}x{}={}".format(n,i,n*i))