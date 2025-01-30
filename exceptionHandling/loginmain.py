from  loginexception import LoginPasswordError,LoginUsernameError
from loginfun import validate
while(True):
    try:
        username=input("enter a names:")
        passwords=input("enter a password:")
        validate(username,passwords)
    except LoginUsernameError:
        print("{} Invalid User Name:".format(username))
    except LoginPasswordError:
        print("{} Invalid Passward".format(passwords))
    else:
        ch = input("\nDo u want to Login with another Details(yes/no):")
        if (ch.lower() == "no"):
            print("Thx for this Program")
            break