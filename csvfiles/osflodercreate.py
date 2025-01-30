#program for creating floder
import os
try:
    os.mkdir("sai.py")
    print("floder created successfully:")
except FileExistsError:
    print("floder already exist")
except FileNotFoundError:
    print("file does not exist")
except OSError:
    print("mkdirs can create only one floder at a time")