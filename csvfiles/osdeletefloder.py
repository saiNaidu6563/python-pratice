#program for deleting specified floder
import os
try:
    os.rmdir("sai")
    print("floder deleted successfully:")

except FileNotFoundError:
    print("file does not exist")
except OSError:
    print("check ur path")