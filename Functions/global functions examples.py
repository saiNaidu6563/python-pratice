# #program for demonstrating local and global vars with different vars
# #exp1
# a=10
# b=20
# c=30
# d=40
# def operation():
#     x=100
#     y=200
#     z=300
#     p=400
#     r=x+y+z+p+a+b+c+d
#     print("sum of both local and global var=",r)
# #main program
# operation()

# #program for demonstrating local and global vars with same vars
# #exp2
# a=10
# b=20
# c=30
# d=40
# def operation():
#     a=100
#     b=200
#     c=300
#     d=400
#     r=a+b+c+d+globals()["a"]+globals()["b"]+globals().get("c")+globals().get("d")
#     print("sum of both local and global var=",r)
# #main program
# operation()

#program for demonstrating local and global vars with same vars
#exp3
a=10
b=20
c=30
d=40
def operation():
    s=globals()
    a=100
    b=200
    c=300
    d=400
    r=a+b+c+d+s["a"]+s["b"]+s.get("c")+s.get("d")
    print("sum of both local and global var=",r)
#main program
operation()