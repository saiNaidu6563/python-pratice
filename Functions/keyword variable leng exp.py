#exp1
#KeyWordVarLenArgsEx1.py
# def  dispvalues(eno,ename,sal,compname): # Function Def-1
# 	print(eno,ename,sal,compname)
#
# dispvalues(eno=10,ename="RS",sal=45.67,compname="PSF") # Function call-1 with 4  Keyword Variable length args
# #------------------------------------------------------------------------------------------------------------------
# def  dispvalues(sno,sname,cm,cppm,pm):  # Function Def-2
# 	print(sno,sname,cm,cppm,pm)
#
# dispvalues(sno=20,sname="Travis",cm=30,cppm=56,pm=58)# Function call-2 with 5 Keyword Variable length  args
# #------------------------------------------------------------------------------------------------------------------
# def dispvalues(tno,tname,subject1,subject2,Subject3,colname): #  Function Def-3
# 	print(tno,tname,subject1,subject2,Subject3,colname)
#
# dispvalues(tno=30,tname="Ritche",subject1="PYTHON",subject2="Java",Subject3="C",colname="JNTU") # Function call-3 with 6  Keyword Variable length  args
# #------------------------------------------------------------------------------------------------------------------
# def dispvalues(cid,cname,job): #  Function Def-4
# 	print(cid,cname,job)
#
# dispvalues(cid=40,cname="Hunter",job="Student")  # Function call-4 with 3  Keyword Variable length  args
# #------------------------------------------------------------------------------------------------------
 #exp2
#KeyWordVarLenArgsEx2.py
# def  dispvalues(**sai): # Function Def-1
# 	print(sai,type(sai))
#
# dispvalues(eno=10,ename="RS",sal=45.67,compname="PSF") # Function call-1 with 4  Keyword Variable length args
# #------------------------------------------------------------------------------------------------------------
# dispvalues(sno=20,sname="Travis",cm=30,cppm=56,pm=58)# Function call-2 with 5 Keyword Variable length  args
# #------------------------------------------------------------------------------------------------------------------
# dispvalues(tno=30,tname="Ritche",subject1="PYTHON",subject2="Java",Subject3="C",colname="JNTU") # Function call-3 with 6  Keyword Variable length  args
# #------------------------------------------------------------------------------------------------------------------
# dispvalues(cid=40,cname="Hunter",job="Student")  # Function call-4 with 3  Keyword Variable length  args
#----
#ep3
def  dispvalues(**sai):# Function Def-1
    print("_" * 50)
    for k, v in sai.items():
        print("\t{}--->{}".format(k, v))
    print("-" * 50)
dispvalues(eno=10,ename="RS",sal=45.67,compname="PSF") # Function call-1 with 4  Keyword Variable length args
#------------------------------------------------------------------------------------------------------------
dispvalues(sno=20,sname="Travis",cm=30,cppm=56,pm=58)# Function call-2 with 5 Keyword Variable length  args
#------------------------------------------------------------------------------------------------------------------
dispvalues(tno=30,tname="Ritche",subject1="PYTHON",subject2="Java",Subject3="C",colname="JNTU") # Function call-3 with 6  Keyword Variable length  args
#------------------------------------------------------------------------------------------------------------------
dispvalues(cid=40,cname="Hunter",job="Student")  # Function call-4 with 3  Keyword Variable length  args
