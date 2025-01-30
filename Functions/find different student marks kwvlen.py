#program for accepting different student marks,different classes and find the sum of marks
# def findtotalmarks(id,sname,cls,**submarks):
#     print('-'*50)
#     print("\t student number:{}".format(id))
#     print("\t student name :{}".format(sname))
#     print("\t student class:{}".format(cls))
#     print('-'*50)
#     if len(submarks)!=0:
#         tot=0
#         for subjects,marks in submarks.items():
#             print("\t{}-->{}".format(subjects,marks))
#             tot=tot+marks
#         print("-"*50)
#         print("\t total marks :{}".format(tot))
#         print("*"*50)
# #Main Program
# findtotalmarks(100,"Praveen","X",telugu=70,hindi=80,english=85,maths=90,science=89,social=80)
# findtotalmarks(200,"Sandeep","XI",Sanskrit=99,Eng=95,Maths=75,Phy=60,Che=58)
# findtotalmarks(300,"Balaji","B.Tech",OS=70,DBMS=60,NW=50,C=59)
# findtotalmarks(400,"Rossum","Research")
#process-2
# def findtotalmarks(id,sname,cls,city="hyd",**submarks):
#     print('-'*50)
#     print("\t student number:{}".format(id))
#     print("\t student name :{}".format(sname))
#     print("\t student class:{}".format(cls))
#     print("\t city:{}".format(city))
#     print('-'*50)
#     if len(submarks)!=0:
#         tot=0
#         for subjects,marks in submarks.items():
#             print("\t{}-->{}".format(subjects,marks))
#             tot=tot+marks
#         print("-"*50)
#         print("\t total marks :{}".format(tot))
#         print("*"*50)
# #Main Program
# findtotalmarks(100,"Praveen","X",telugu=70,hindi=80,english=85,maths=90,science=89,social=80)
# findtotalmarks(200,"Sandeep","XI",Sanskrit=99,Eng=95,Maths=75,Phy=60,Che=58)
# findtotalmarks(300,"Balaji","B.Tech",OS=70,DBMS=60,NW=50,C=59)
# findtotalmarks(cls="Research",sname="Rossum",city="NL",id=400)
# findtotalmarks(500,"Shankar","V",Tel=50,Eng=60,Maths=70,abacus=40,city="FINLAND")
# findtotalmarks(600,"Athar","MCA","AP",AI=40,CG=60)

#procces-3
def findtotalmarks(id,sname,cls,*vals,city="hyd",**submarks):
    print('-'*50)
    print("\t student number:{}".format(id))
    print("\t student name :{}".format(sname))
    print("\t student class:{}".format(cls))
    print("\t city:{}".format(city))
    print("\t variable length args:{} and length:{}".format(vals,len(vals)))
    print('-'*50)
    if len(submarks)!=0:
        tot=0
        for subjects,marks in submarks.items():
            print("\t{}-->{}".format(subjects,marks))
            tot=tot+marks
        print("-"*50)
        print("\t total marks :{}".format(tot))
        print("*"*50)
#Main Program
findtotalmarks(100,"Praveen","X",10,13,14,9,17,15,telugu=70,hindi=80,english=85,maths=90,science=89,social=80)
findtotalmarks(200,"Sandeep","XI",2.3,4.5,5.6,6.7,5,Sanskrit=99,Eng=95,Maths=75,Phy=60,Che=58)
findtotalmarks(300,"Balaji","B.Tech","A","B","C","D",OS=70,DBMS=60,NW=50,C=59)
findtotalmarks(400,"Rossum","Research",1,2,3,city="NL")
findtotalmarks(500,"Shankar","V",Tel=50,Eng=60,Maths=70,abacus=40,city="FINLAND")
findtotalmarks(600,"Athar","MCA",11,22,city="AP",AI=40,CG=60)