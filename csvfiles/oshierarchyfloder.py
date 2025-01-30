#program for creating hierarchy floder
import os
try:
    os.makedirs("emp\\ name\\sal\\id.py")
    print("floder created successfully:")
except FileExistsError:
    print("floder already exist")
except FileNotFoundError:
    print("file does not exist")
except OSError:
    print(" check ur path")