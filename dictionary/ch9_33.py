fruits = {"apple": 30, "orange": 10, "banana": 5}
ret_value = fruits.pop("apple")
print(fruits)

ret_value2 = fruits.pop("grape", "does not exits")
print(ret_value2)
print(fruits)