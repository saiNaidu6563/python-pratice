#convert dict data to jsonfile data
import json
dcdata={"sno":100,"name":"sai","sal":3.45,"dsg":"se"}
print("*"*50)
with open("jdata.json","w") as fp:
    jdata=json.dump(dcdata,fp)
    print("dict data saved in json file")