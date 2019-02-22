import json

listNumbers = [5, 10, 20, 1]
tupleNumbers = (1, 5, 6, 9)
jsonData1 = json.dumps(listNumbers)
jsonData2 = json.dumps(tupleNumbers)
print(listNumbers)
print(type(listNumbers))
print(tupleNumbers)
print(type(tupleNumbers))
print("----------------------------------")
print(jsonData1)
print(type(jsonData1))
print(jsonData2)
print(type(jsonData2))