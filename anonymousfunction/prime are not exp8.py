#program for accepting number prime are not
# p=lambda a:all( a%i!=0 for i in range (2,int(a**0.5)+1)) and a>1
# a=float(input("enter a value:"))
# result = "prime" if p(a) else "not prime"
# print(result)

prime = lambda a: "{} is a prime number".format(a) if a > 1 and all(a % i != 0 for i in range(2, int(a**0.5) + 1)) else "{} is not a prime number".format(a)

# Main Program
num = int(input("Enter any number: "))
print(prime(num))