#programfor demonstrating the need for break statement
# s="MISSISSIPPI"
# for v in s:
#     print(v)
# else:
#     print("I am from else part of for loop")
#     print("----------------------------------")
#     ctr=0
#     for v in s:
#         if v == "I":
#             ctr = ctr + 1
#             if ctr == 2:
#                 break
#         print(v, end="")


#by using while loop
s="MISSISSIPPI"
i=0
while i<len(s):
    print(s[i])
    i=i+1

else:
    print("*"*50)
    ctr=0
    i=0
    while i < len(s):
        if s[i]=="I":
            ctr=ctr+1
            if ctr==2:
                break
        print(s[i])
        i = i + 1
