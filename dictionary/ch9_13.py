# 字典的複製
fruits = {"apple": 30, "orange": 10, "banana": 15}
cfruits = fruits.copy()
print("位址:", id(fruits), "元素", fruits)
print("位址:", id(cfruits), "元素", cfruits)