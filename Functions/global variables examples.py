#program for demonstrating global variables
# #exp1
# def learnAI():
#     sub1="AI"
#     print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub1,lang))
# def learnMl():
#     sub2="Ml"
#     print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub2,lang))
# def learnds():
#     sub3="DS"
#     print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub3,lang))
# lang="python"
# learnAI()
# learnMl()
# learnds()

# #exp2
# lang="python"
# def learnAI():
#     sub1="AI"
#     print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub1,lang))
# def learnMl():
#     sub2="Ml"
#     print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub2,lang))
# def learnds():
#     sub3="DS"
#     print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub3,lang))
# learnAI()
# learnMl()
# learnds()

#exp3
# def learnAI():
#     sub1="AI"
#     print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub1,lang))
# lang="python"
# def learnMl():
#     sub2="Ml"
#     print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub2,lang))
# def learnds():
#     sub3="DS"
#     print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub3,lang))
# learnAI()
# learnMl()
# learnds()

#exp4
def learnAI():
    sub1="AI"
    print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub1,lang))
def learnMl():
    sub2="Ml"
    print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub2,lang))
def learnds():
    sub3="DS"
    print("To Develop '{}' Based Applications, we use '{}' Programming Lang".format(sub3,lang))
#learnAI()--->we can't access 'lang' inside of learnAI() bcoz 'lang' defined after function call
lang="python" #global var
learnMl()
learnds()