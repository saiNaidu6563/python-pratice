#program for accepting list of numbers and find there squares and square roots
lst=list(map(float,input("enter list of values separated by space:").split()))
sq=list(map(lambda v:v**2,lst))
sqr=list(map(lambda v:v**0.5,lst))
print("*"*50)
print("\tgiven values\t\tsquares\t\tsquare roots")
print("*"*50)
for g,q,qr in zip(lst,sq,sqr):
    print("\t{}\t\t\t\t{}\t\t\t\t{}".format(g,q,round(qr,2)))
print("*"*50)