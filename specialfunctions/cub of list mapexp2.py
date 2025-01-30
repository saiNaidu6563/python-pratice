#program for accepting list of numbers and find there cubes
lst=list(map(float,input("enter list of values separated by space:").split()))
c=list(map(lambda v:v**3,lst))
print("*"*50)
print("\tgiven values\t\tcube values")
print("*"*50)
for g,cu in zip(lst,c):
    print("\t{}\t\t\t\t\t\t{}".format(g,cu))
print("*"*50)