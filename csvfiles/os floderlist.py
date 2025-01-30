#program for list the files in floder
import os
try:
    fn=input("enter floder name:")
    fl=os.listdir(fn)
    for val in fl:
        print(val)
except FileNotFoundError:
    print("file does not exist")
except OSError:
    print("check ur path")