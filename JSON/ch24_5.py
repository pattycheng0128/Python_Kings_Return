import json

jsonObj = '{"b": 80, "a": 25, "c": 60}'
dictObj = json.loads(jsonObj)
print(type(jsonObj))
print("-------------------")
print(dictObj)
print(type(dictObj))