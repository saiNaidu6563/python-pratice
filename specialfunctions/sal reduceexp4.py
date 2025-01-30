import functools
from traceback import format_list

od=list(map(float,input("enter the list of salaries separated by space:").split()))
print("given list=",od)
print("-"*80)
sal0_500=list(filter(lambda sal:0<=sal<=500,od))
hikesal=list(map(lambda sal:sal+sal*(10/100),sal0_500))
print("*"*50)
print("salary range0 to 500\t\thike salary ")
print("*"*50)
for k,v in zip(sal0_500,hikesal):
    print("\t\t{}\t\t\t{}".format(k,v))
print("*"*50)
tsal=functools.reduce(lambda sal1,sal2:sal1+sal2,sal0_500)
thike=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal)
print(" Total:{}\t\t\t{}".format(tsal,thike))
print("*"*50)
sal500_1000=list(filter(lambda sal:sal in range(501,1001),od))
hikesal500=list(map(lambda sal:sal+sal*(20/100),sal500_1000))
print("*"*50)
for osl,hsl in zip(sal500_1000,hikesal500):
    print("\t{}\t\t\t{}".format(osl, hsl))
print("*"*50)
tsal500=functools.reduce(lambda k,v:k+v,sal500_1000)
hike500=functools.reduce(lambda k,v:k+v,hikesal500)
print(" Total:{}\t\t\t{}".format(tsal500,hike500))
print("*"*50)
print("grand total\t{}\t{}".format(tsal+tsal500,thike+hike500))
print("*"*500)


# import functools
# oldsal=list([float(sal) for sal in input("Enter List of Salaries:").split()   if float(sal) in range(0,1001) ] )
# print("-------------------------------------------------------------------------------")
# print("Given Salaries:")
# print(oldsal)
# print("-------------------------------------------------------------------------------")
# #Get the salaries ranges from 0 to 500 and give 10 % hike
# sal0_500=list(filter(lambda sal: 0<=sal<=500, oldsal))
# hikesal0_500=list(map(lambda sal:sal+sal*(10/100),sal0_500))
# print("*"*50)
# print("Salaries ranges 0 -500\tHike Salaries ranges 0 -500")
# print("*"*50)
# for osl,hsl in zip(sal0_500,hikesal0_500):
# 	print("\t{}\t\t\t{}".format(osl,hsl))
# print("*"*50)
# #Find the Total Salary before hike and after hike whose  salaries ranges from 0 to 500
# totsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2, sal0_500)
# hiketotsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2, hikesal0_500)
# print(" Total:{}\t\t\t{}".format(totsal0_500,hiketotsal0_500))
# print("*"*50)
# #Get the salaries ranges from 501 to 1000 and give 20 % hike
# sal501_1000=list(filter(lambda sal: sal in range(501,1001), oldsal))
# hikesal501_1000=list(map(lambda sal:sal+sal*(20/100),sal501_1000))
# print("*"*50)
# print("Salaries ranges 501-1000\tHike Salaries ranges 501 -1000")
# print("*"*50)
# for osl,hsl in zip(sal501_1000,hikesal501_1000):
# 		print("\t{}\t\t\t{}".format(osl,hsl))
# print("*"*50)
# totsal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,sal501_1000)
# tothikesal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal501_1000)
# print(" Total:{}\t\t\t{}".format(totsal501_1000,tothikesal501_1000))
# print("*"*50)
# print("Grand Totals:{}\t\t\t{}".format(totsal0_500+totsal501_1000,hiketotsal0_500+tothikesal501_1000))
# print("*"*50)