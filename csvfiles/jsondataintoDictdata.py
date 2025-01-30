#convert json data into dict data
import json
jdata='{"id":"100","name":"sai","sal":"3.45","dsg":"se"}'
print("*"*50)
data=json.loads(jdata)
print("*"*50)
for v,k in data.items():
    print("{}==>{}".format(v,k))