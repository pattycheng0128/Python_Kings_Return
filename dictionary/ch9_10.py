fruits = {"apple": 30, "orange": 10, "banana": 15}
print("印出舊的資料", fruits)
# 針對指定元素做刪除
del fruits["apple"]
print("印出刪除後的資料", fruits)

# 刪除所有元素
fruits.clear()
print("刪除所有元素:", fruits)