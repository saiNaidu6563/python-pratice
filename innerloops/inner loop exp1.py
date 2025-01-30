#inner loop example--->for loop
for v in range (1,6):
    print(v)
    print("*"*50)
    for i in range(1,4):
        print(i)
    else:
        print("iam part of inner loop")
        print("*" * 50)
else:
    print("iam part of outer loop")