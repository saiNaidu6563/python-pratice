import pickle
def dsearch():
         empno=int(input("enter employee number:"))
         lst = []
         with open("employee.info","rb") as fp:
             while (True):
                 try:
                     record = pickle.load(fp)
                     lst.append(record)
                 except EOFError:
                     break
             r = False
             for v in lst:
                 if v[0] == empno:
                     r = True
                     break
             if r:
                 print("\t{} Employee Number  Exist".format(empno))
             else:
                 print("\t{} Employee Number Does not Exist".format(empno))



