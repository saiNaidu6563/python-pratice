#program for accepting list of values and find second height values
def readlst():
    n=int(input("enter a value which you want:"))
    if n<=0:
        return []
    else:
        lst=[]
        for i in range(1,n+1):
            val=float(input("enter {} value:".format(i)))
            lst.append(val)
        return lst
def second():
    lst=readlst()
    if len(lst)==0:
        print("invalid input")
    else:
        s=sorted(set(lst))
        print(s)
        print("runner of lst:{}".format(s[-2]))
#main program
second()
# def getscores():
#     scores=[]
#     noc=int(input("Enter Number of Scores:"))
#     if(noc<=0):
#         return scores
#     else:
#         for i in range(1,noc+1):
#             scores.append(float(input("Enter {} Score Value:".format(i))))
#         else:
#             return scores
#
# def getrunnerupscore():
#     scores=getscores()
#     if(len(scores)==0):
#         print("There is no score--can't find runner up score")
#     else:
#         score=sorted(set(scores))
#         print("Unique Score Values")
#         print(score)
#         print("Runner-up score={}".format(score[-2]))
# #main program
# getrunnerupscore()



