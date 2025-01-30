#Program for Accepting List of Values and Find Max and Min by using Anonymous Functions
# with pre-functions max() and min()
def readvalues():
    n = int(input("enter a value u want:"))
    if n<=0:
        return []
    else:
        lst=[]
        for i in range(1,n+1):
            lst.append(float(input("enter {} value:".format(i))))
        else:
            return lst
finmax=lambda lst:max(lst)
finmin=lambda lst:min(lst)
#main program

lst=readvalues()
if len(lst)==0:
    print("is invalid input")
else:
    r=finmax(lst)
    r1=finmin(lst)
    print(f"max value:{r}")
    print(f"min value:{r1}")