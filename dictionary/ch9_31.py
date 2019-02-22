# setdefault功能，已存在的內容會保持不變，不存在的內容會加入內容
fruits = {"apple": 30, "orange": 10}
ret_value1 = fruits.setdefault("apple")
print(fruits)

ret_value2 = fruits.setdefault("grape", 60)
print(fruits)

ret_value3 = fruits.setdefault("banana", 10)
print(fruits)