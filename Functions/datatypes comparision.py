#program for displaying different types of values in a single function with data type comparision
def dispval(x):
    if type(x)==int:
        print("{} is type{}".format(x,type(x)))
    elif type(x)==float:
        print("{} is type{}".format(x,type(x)))
    elif type(x)==bool:
        print("{} is type{}".format(x,type(x)))
    elif type(x)==complex:
        print("{} is type{}".format(x,type(x)))
    elif type(x)==str:
        print("{} is type{}".format(x,type(x)))
    elif type(x)==bytes:
        print("{} is type{}".format(x,type(x)))
    elif type(x)==bytearray:
        print("{} is type{}".format(x,type(x)))
    elif type(x)==range:
        print("{} is type{}".format(x,type(x)))
        for i in x:
            print(i)
    elif type(x) == list:
        print("{} is type{}".format(x, type(x)))
    elif type(x) == tuple:
        print("{} is type{}".format(x, type(x)))
    elif type(x) == set:
        print("{} is type{}".format(x, type(x)))
    elif type(x) == frozenset:
        print("{} is type{}".format(x, type(x)))
    elif type(x) == dict:
        print("{} is type{}".format(x, type(x)))
        for v,l in x.items():
            print("{}-->{}".format(v,l))
    else:
        print("{} is type{}".format(x, type(x)))


#mainprogram
print("*"*50)
print("fundamental category:")
dispval(10)
dispval(10.4)
dispval(True)
dispval(2+3j)
print("*"*50)
print("sequence category:")
dispval("sai")
dispval(bytes([1,18,45]))
dispval(bytearray([1,218,18,45]))
dispval(range(10,22,2))
print("*"*50)
print("list category:")
dispval([1,45,67,18])
dispval((1,17,18,45))
dispval(list("PYTHON")) # Function with list type
dispval(tuple("TUPLE"))
print("*"*50)
print("set category:")
dispval({14,34,45,18,7})
dispval(frozenset({45,18,7,1}))
print("*"*50)
print("dict category")
dispval({1:"sai",2:"priya",3:45})
dispval(dict([(10,"RS") ,(20,"TR"),(30,"DR")]))# Function with dict type
dispval(dict(zip( ["Python","C","C++","Java"],[1,2,3,4] )))
print("*"*50)
dispval(None)