import json

dictObj = {"b": 80, "a": 25, "c": 60}
jsonData = json.dumps(dictObj, sort_keys=True, indent=4)
print(jsonData)
