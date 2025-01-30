#inner loop example--->for loop in while loop
i=1
while(i<=5):
    print(i)
    print("*" * 50)
    for j in range(3,0,-1):
        print(j)
    else:
        i = i + 1
        print("iam part of inner loop")
        print("*" * 50)
else:
    print("iam part of outer loop")

