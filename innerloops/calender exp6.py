#program for generating 1 to 12 months calenders
import calendar
year=int(input("enter year number you want:"))
if year<=0:
    print("{} is invalid input".format(year))
else:
    print(year)
    for i in range(1,13):
        print(calendar.month(year,i))
        print("*"*50)