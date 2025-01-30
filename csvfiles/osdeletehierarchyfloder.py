#program deleting hierarchy floder
import os
try:
    os.removedirs("emp\\ name\\sal\\id.py")
    print("floder deleted successfuly:")
except FileNotFoundError:
    print("floder does not exist")
except OSError:
    print("check ur path")