from loginexception import LoginPasswordError,LoginUsernameError
def welcome(uname):
    print("Hi {}, Good Morning-Good Remberence about user name and Pwd".format(uname))
# def validate(uname,password):
#     username=["python","Java","c"]
#     passwords=["Rossum","James","Richey"]
#     if uname not in username:
#         raise LoginUsernameError
#     elif password not in passwords:
#         raise LoginPasswordError
#     else:
#         welcome(uname)
def validate(uname,pwd):
    u={"python":"Rossum","java":"James","c":"Richey"}
    # p={1:"Rossum",2:"James",3:"richey"}
    if uname not  in u.keys():
        raise LoginUsernameError
    elif pwd not in u.values():
        raise LoginPasswordError
    else:
        welcome(uname)