#program for removing specific file name
import os
try:
    os.remove("sai")
    print("file deleted successully")
except FileNotFoundError:
    print("file does not exist")
except OSError:
    print("check u r path")