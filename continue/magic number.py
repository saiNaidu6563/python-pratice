#program for accepting numerical number and decide whether it is magic number are not
# Accept a numerical value from the user
num = int(input("Enter a number to decide whether it is magic or not: "))
ns = str(num)
sq = str(num ** 2)
res = f"{num} is a magic number." if num != 0 and ns == sq[-len(ns):] else f"{num} is not a magic number."
print(res)

