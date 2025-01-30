#exp1
# def disp(a,b,c,d):
#     print("\t{}\t{}\t{}\t{}".format(a,b,c,d))
# #mainprogram
# print("-"*50)
# print("\tA\tB\tC\td")
# print("_"*50)
# disp(10,20,30,40)#function call with pos args
# disp(b=20,d=40,c=30,a=10)#function call with keyword args
# disp(c=30,d=40,a=10,b=20)#function call with keyword args
# disp(10,20,d=40,c=30)#function call with pos and keyword args

#exp2
# def disp(a,b,c,d,city="hyd"):
#     print("\t{}\t{}\t{}\t{}\t{}".format(a,b,c,d,city))
# #mainprogram
# print("-"*50)
# print("\tA\tB\tC\td\tcity")
# print("_"*50)
# disp(10,20,30,40)#function call with pos args
# disp(b=20,d=40,c=30,a=10)#function call with keyword args
# disp(c=30,d=40,a=10,b=20)#function call with keyword args
# disp(10,20,d=40,c=30)#function call with pos and keyword args
# disp(city="tpd", d=40,c=30,a=10,b=20)
# disp(d=40,c=30,a=10,b=20,city="tpd")
# disp(10,20,d=40,city="tpd",c=30)

#variable length args
#exp1
# def disp(*kvr):
#     print(kvr,type(kvr))
# #mainprogram
# disp(10,20,30,40,50)
# disp(10,20,30,40)
# disp(10,20,30)
# disp(10,20)
# disp(10)
# disp()

#exp2
# def disp(*kvr):
#     if len(kvr)==0:
#         print("empty")
#     else:
#         for v in kvr:
#             print("{}".format(v),end=" ")
#         print()
# #mainprogram
# disp(10,20,30,40,50)
# disp(10,20,30,40)
# disp(10,20,30)
# disp(10,20)
# disp(10)
# disp()
#exp3
# def disp(sno,sname,*kvr):
#     print("student number:{}".format(sno))
#     print("student name:{}".format(sname))
#     print("*"*50)
#     s=0
#     for v in kvr:
#         print("{}".format(v))
#         s=s+v
#     else:
#         print("sum={}".format(s))
# #mainprogram
# disp(100,"rossum",10,20,30,40,50)
# disp(200,"hunter",10,20,30,40)
# disp(300,"james",10,20,30)
# disp(400,"ststrup",10,20)
# disp(500,"travils")

#exp4
def disp(sno,sname,*kvr,city="hyd"):
    print("student number:{}".format(sno))
    print("student name:{}".format(sname))
    print("city name:{}".format(city))
    print("*"*50)
    s=0
    for v in kvr:
        print("{}".format(v))
        s=s+v
    else:
        print("sum={}".format(s))
#mainprogram
disp(100,"rossum",10,20,30,40,50)
disp(200,"hunter",10,20,30,40)
disp(300,"james",10,20,30)
disp(400,"ststrup",10,20)
disp(500,"travils")
disp(600,"kvr",40,50,60,80,city="ap")
