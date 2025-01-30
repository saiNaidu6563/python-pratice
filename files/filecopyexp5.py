#program for accepting copy the image into another file
try:
    with open("C:\\Users\\Intel\\OneDrive\\Pictures\\Saved Pictures\\hunuman.jpg","rb") as rp:
        with open("stud5.data","ab") as wp:
            rc=rp.read()
            wp.write(rc)
            print("img is copyed")
except FileNotFoundError:
    print("file is not exists")