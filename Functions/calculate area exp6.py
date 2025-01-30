#program for calculating area of square ,rectangle,circle,Triangle by using functions
def sqarea(s):

    if s<=0:
        return "invalid input"
    ars=s**2
    return s,ars
#area of rectangle
def recarea():
    l=float(input("enter length:"))
    b=float(input("enter breadth:"))
    if l<=0 or b<=0:
        return "invalid input"
    arrct=l*b
    print("*" * 50)
    print("area of rectangle :{},{}={}".format(l, b, arrct))
    print("*" * 50)


#area of circle
def cirarea(r):
    # r=float(input("enter radius :"))
    if r<=0:
        return "invalid input"
    arcir=3.14*r**2
    print("area of circle{}={}".format(r,arcir))

#area of triangle
def trarea():
    b=float(input("enter breath:"))
    h=float(input("enter height:"))
    if b<=0 or h<=0:
        return "invalid input"
    artr=1/2*b*h
    return b,h,artr

print("="*50)
#mainprogram
s=float(input("enter side of square:"))
s,sr=sqarea(s)
print("*"*50)
print("area of square:{}={}".format(s,sr))
print("*"*50)
recarea()
print("*"*50)
r=float(input("enter radius :"))
cirarea(r)
print("*"*50)
b,h,trar=trarea()
print("*"*50)
print("area triangle{},{}={}".format(b,h,trar))
print("="*50)