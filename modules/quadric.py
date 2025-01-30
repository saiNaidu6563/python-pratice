#program for accepting quadratic equation
import cmath
def root():
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    c=int(input("enter c value:"))
    d=cmath.sqrt(b**2-4*a*c)
    s1=(-b+d)/2*a
    s2=(-b-d)*0.5/2*a
    print("the roots quadratic equation are:{}and:{}".format(s1,s2))
root()