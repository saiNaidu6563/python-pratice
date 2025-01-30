#conert json file data into dict data
import json
try:
    with open("jdata.json","r") as fp:
        data=json.load(fp)
        for k,v in data.items():
            print("{}===>{}".format(k,v))
except FileNotFoundError:
    print("file does not exit")