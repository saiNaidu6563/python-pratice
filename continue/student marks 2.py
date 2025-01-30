#program for accepting student marks
while(True):
    while(True):
        sno=input("enter student number:")
        if sno.isdigit() and (int (sno) in range(100,201)):
            break
        else:
            print("{} is invalid number".format(sno))
    while(True):
        name=input("enter a name:")
        words=name.split()
        nv=True
        for word in words:
            if ( not word.isalpha()):
                nv=False
                break
        if nv:
            break
        else:
            print("{} is invalid".format(name))
    while(True):
        cm=input("enter c lang marks:")
        if cm.isdigit() and (int(0<=int(cm)<=100)):
            break
        else:
            print("{} is invalid c marks".format(cm))
    while (True):
        cppm = input("enter c++ lang marks:")
        if cm.isdigit() and (int(0 <= int(cppm) <= 100)):
            break
        else:
            print("{} is invalid c++ marks".format(cm))
    while (True):
        pym = input("enter python lang marks:")
        if cm.isdigit() and (int(0 <=int(pym)<= 100)):
            break
        else:
            print("{} is invalid python marks".format(cm))
    total=int(cm)+int(cppm)+int(pym)
    percentage=(total/300)*100
    if(int(cm)<40)or(int(cppm)<40)or(int(pym)<40):
        grade="FAIL"
    else:
            if (percentage in range(75,101)):
                grade="DISTINCTION"
            elif (percentage in range(60,75)):
                grade="FIRST"
            elif (50<=percentag<=59):
                grade="SECOND"
            elif (40<=percentage<=49) :
                grade="THIRD"
    print("*"*70)
    print("STUDENT MARK REPORT:")
    print("*"*70)
    print("student number:{}".format(sno))
    print("student name:{}".format(name))
    print("{} student marks in c:".format(cm))
    print("{} student marks in c++:".format(cppm))
    print("{} student marks in python:".format(pym))
    print("{} student grade:".format(grade))
    print("*"*70)
    ch=input("DO U WANT ANY ANOTHER STUDENT DATA(YES/NO):")
    if ch.upper()=="NO":
        print("THANKS FOR USING PROGRAM:")
        break



