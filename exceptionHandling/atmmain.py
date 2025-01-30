from atmfun import  deposit,withdraw,balenq
from atmexception import DepositError, InsufficientError

while(True):
    try:
        ch=int(input("Enter you are choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("Don't enter -ve values:")

            case 2:
                try:
                    withdraw()
                except WindowsError:
                    print("Don't enter -ve values:")
                except InsufficientError:
                    print("insuficent fund not requeried balance ")
            case 3:
                balenq()
            case 4:
                print("thanks for using this operation")
                break
            case _:
                print("You are selection of operation is wrong--->try again:")
    except ValueError:
        print("Don't Enter alnum, special symbols and strs:")