import json

dictObj = {"b": 80, "a": 25, "c": 60}
jsonObj1 = json.dumps(dictObj)  # 由字典轉換為json是無序資料
jsonObj2 = json.dumps(dictObj, sort_keys=True)  # 透過sort_keys=True來做排序
print(jsonObj1)
print(jsonObj2)

print(jsonObj1 == jsonObj2)
print(type(jsonObj1))

