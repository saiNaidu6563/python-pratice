s = int(input("enter a list of number:"))
if s == 0:
    print("invalid input:")
else:

    lst = []
    for i in range(1,s+1):
        lst.append(float(input("enter {} value:".format(i))))
        print(lst)
    else:
        print("*"*50)
        lst.pop()
        print(lst)
        print("*" * 50)
        lst.clear()
        print(lst)
        del lst[::]
        print(lst)
