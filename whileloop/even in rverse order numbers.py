#program for generating even number in reverse within n where n is positive number
n = int(input("Enter a positive number n: "))
if n <= 0:
    print("{} is an invalid input".format(n))
else:
    print("*" * 50)
    print("List of even numbers within {} in reverse order:".format(n))
    if n % 2 != 0:  # If n is odd, start from n-1
        n = n - 1
    i = n
    while i >= 0:
        print(i)
        i = i - 2
    print("Program completed")
    print("*" * 50)
