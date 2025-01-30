#program for demonstring the need for break statement
# s="python"
# for ch in s:
#     print(ch)
# else:
#     print("iam else part of for loop")
#     print("*"*50)
#     for ch in s:
#         if ch=="t":
#             continue
#         print(ch)
#     else:
#         print("iam else part of for loop")


#by using while loop
# s="python"
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+1
# else:
#     print("iam else path of while loop")
#     print("*"*50)
# i=0
# while i<len(s):
#     if s[i] == "t":
#         i = i + 1
#         continue
#     print(s[i], end="")
#     i = i + 1
#
# else:
#     print("\n iam else path of while loop")


# s="python"
# for ch in s:
#     print(ch)
# else:
#     print("iam else part of for loop")
#     print("*"*50)
#     for ch in s:
#         if ch in ["t","o"]:
#             continue
#         print(ch)
#     else:
#         print("iam else part of for loop")
#


#by using while loop
s="python"
i=0
while i<len(s):
    print(s[i])
    i=i+1
else:
    print("iam else path of while loop")
    print("*"*50)
i=0
while i<len(s):
    if s[i] in["t","o"]:
        i = i + 1
        continue
    print(s[i], end="")
    i = i + 1

else:
    print("\n iam else path of while loop")

