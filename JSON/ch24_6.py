import json

dictObj = {"a": 40, "b": 30, "c": 10}
fn = "out24_6.json"
with open(fn, "w") as fnObj:
    json.dump(dictObj, fnObj)