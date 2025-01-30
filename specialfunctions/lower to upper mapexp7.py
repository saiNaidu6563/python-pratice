#program for converting lower case to upper case accepting words from keyboard
print("enter list of word separated by space:")
lst=list(map(str,input().split()))
up=list(map(lambda a:a.upper(),lst))
print("*"*50)
print("\t lst1\tuppercase words")
print("*"*50)
for i,j in zip(lst,up):
    print("\t{}\t\t{}".format(i,j))
print("*"*50)