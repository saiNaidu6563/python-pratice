#program for accepting list of words and find there reverse
lst=list(map(str,input("enter list of words separated by coma:").split(",")))
w=list(map(lambda word:word.isalpha()and word[::-1],lst))
print("*"*50)
print("\tgiven words\t\treversed values")
print("*"*50)
for gw,wr in zip(lst,w):
    print("\t{}\t\t\t\t\t\t{}".format(gw,wr))
print("*"*50)