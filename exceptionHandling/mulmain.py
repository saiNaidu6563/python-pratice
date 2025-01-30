from mulexception import NegativeError,ZeroError
from mulfun import table
while(True):
    try:
        n=int(input("enter a number:"))
        table(n)
    except NegativeError:
        print("Don't enter -ve values: ")
    except ZeroError:
        print("Don't enter zero fro table:")
    except ValueError:
        print("Don't enter alnums,special symbols:")
    except:
        print("ooops,some thing went wrong:")
    else:
        ch=input("if you another number table (yes/no):")
        if ch.lower()=="no":
            print("thx for using program")
            break
