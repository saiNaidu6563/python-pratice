import os
try:
    os.rename("sai.py","mani.py")
    print("rename successfully")

except FileNotFoundError:
    print("file does not exist")
except OSError:
    print("check ur path")
