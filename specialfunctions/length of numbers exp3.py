#program for accepting list of numbers and get those numbers whose length range between 2&3
print("enter a list of numbers separated by space:")
n=[v for v in input().split()]
l=list(filter(lambda val:val.isdigit() and len(val) in [2,3],n))
print("given list of numbers=",n)
print("len of value=",l)