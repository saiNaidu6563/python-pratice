#program for calculating simple interest and total amount to pay
def simpleof():
    p = float(input("enter principle value:"))
    t = float(input("enter time:"))
    r = float(input("enter rate of interest:"))
    lst=[]
    if p<=0:
        lst.append("{} is invalid principle amount".format(p))
    if t <= 0:
        lst.append("{} is invalid time".format(t))
    if r<=0:
        lst.append("{} is invalid rate of interest ".format(p))
    if p<=0 or t<=0 or r<=0:
        return ("".join(lst))
    else:
        s = (p * t * r) / 100
        total = p + s
        return p, t, r, s, total
# mainprogram
r = simpleof()
print(r)
if (type(r) == str):
    print(r)
else:
        print("===========================================")
        print("\t\t\tSimple Interest Calculations")
        print("===========================================")
        print("\t\tPrinciple Amount:{}".format(r[0]))
        print("\t\tTime:{}".format(r[1]))
        print("\t\tRate of Interest:{}".format(r[2]))
        print("\t\tSimple Interest:{}".format(r[3]))
        print("\t\tTotal Amount to Pay:{}".format(r[4]))



