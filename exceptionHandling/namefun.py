from nameexception import InvalidNameError,SpaceError,ZeroError

def validate(n:str):
    if len(n)==0:
        raise ZeroError
    elif n.isspace():
        raise SpaceError
    else:
        w=n.split()
        r=True
        for i in w:
            if  not i.isalpha():
                r=False
                break
        if r:
            return n
        else:
            raise InvalidNameError