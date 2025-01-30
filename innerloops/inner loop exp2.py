#inner loop example--->while loop
i=1
while(i<=5):
    print(i)
    j=1
    print("*"*50)
    while(j<=3):
        print(j)
        j=j+1
    else:
        i=i+1
        print("iam part of inner loop")
        print("*" * 50)
else:
    print("iam part of outer loop")

