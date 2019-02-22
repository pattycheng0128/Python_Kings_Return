import json

fn = "out24_6.json"
with open(fn, "r") as fnObj:
    data = json.load(fnObj)

print(data)