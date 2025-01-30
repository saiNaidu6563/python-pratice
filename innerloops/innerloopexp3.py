#inner loop example--->while loop in for loop
for v in range (1,6):
    print(v)
    print("*"*50)
    i=3
    while(i>=1):
        print(i)
        i=i-1
    else:
        print("iam part of inner loop")
        print("*" * 50)
else:
    print("iam part of outer loop")