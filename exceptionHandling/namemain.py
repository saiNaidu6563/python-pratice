from nameexception import InvalidNameError,SpaceError,ZeroError
from namefun import validate
try:
    n=input("enter a name separated by space:")
    r=validate(n)
except InvalidNameError:
    print("{} is invalid input".format(n))
except SpaceError:
    print("Don't enter empty spc=ace:")
except ZeroError:
    print("Don't enter empty space:")
else:
    print("{} is valid name".format(r))