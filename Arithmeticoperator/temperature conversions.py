#temoerature conversions
#The temperature conversion formula from Celsius to Kelvin is:
c= float(input("enter the value of celsius c:"))
k = c + 273.15
print("\t\t conversion of celsius to kelvin {}={}".format(c,k))
print("*"*30)
# The temperature conversion formula from Kelvin to Celsius is:
k = float(input("enter the value of kelvin k:"))
c=k-273.15
print("\t\t conversion of kelvin to celsius {}={}".format(k,c))
print("*"*30)
#The temperature conversion formula from Fahrenheit to Celsius is:
F=float(input("enter the value of Fahrenheit F:"))
C = (F-32)*5/9
print("\t\t conversion of fahrenheit to celsius {}={}".format(k,c))
print("*"*30)
# The Temperature Conversion Formula from Celsius to Fahrenheit is:
c=float(input("enter the value of celsius c:"))
F = c*(9/5)+32
print("\t\t conversion of  celsius to fahrenheit {}={}".format(c,F))
print("*"*30)
#The Temperature Conversion Formula from Fahrenheit to Kelvin is:
F=float(input("enter the value of Fahrenheit F:"))
k=  (F-32) * 5/9+ 273.15
print("\t\t conversion of  fahrenheit to kelvin {}={}".format(F,k))
print("*"*30)
#The Temperature Conversion Formula from Kelvin to Fahrenheit is:
k=float(input("enter the value of kelvin k:"))
F= (k -273.15) * 9/5 + 32
print("\t\t conversion of kelvin to fahrenheit{}={}".format(k,F))
print("*"*30)