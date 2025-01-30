#programfor demonstrating the need for break statement
#by using for loop
# s="python"
# for ch in s:
#     print(ch)
# else:
#     print("I am from else part of for loop")
#     print("----------------------------------")
# # My Requirement is to display only "PYTH" without using Indexing and Slicing
# print("By using for loop with break")
# for ch in s:
#     if ch=="o":
#         break
#     print(ch,end="")
# else:
#     print("I am from else part of for loop")
# print()
# print("Other statements in Program")
#

#by using while loop
s="python"
i=0
while i<len(s):
    print(s[i])
    i=i+1
else:
    print("*" * 50)
    i=0
    while i < len(s):
        if s[i] =="o":
            break
        print(s[i])
        i = i + 1


