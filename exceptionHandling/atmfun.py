from atmexception import DepositError, WithdrawError, InsufficientError

bal=500
def deposit():
    damt=int(input("enter a deposit amount:"))
    global bal
    if damt <=0:
        raise DepositError
    else:
        bal= bal+damt
        print("you are account xxxxx123 is created by amount is:{}".format(damt))
        print("Avaible balance in are account xxx123 balance is {}".format(bal))
def withdraw():
        global bal
        amt=int(input("Enter a withdraw amount:"))
        if amt<=0:
            raise WithdrawError
        elif amt+500>bal:
            raise InsufficientError
        else:

            bal=bal-amt
            print("you are account xxxxx123 is withdraw by amount is:{}".format(amt))
            print("Avaible balance in are account xxx123 balance is {}".format(bal))
def balenq():
    print("Avaible balance in are account xxx123 balance is {}".format(bal))

