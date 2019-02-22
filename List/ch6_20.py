cars = []
print(cars)
# append()增加元素
cars.append("Benz")
print(cars)
cars.append("Honda")
print(cars)
cars.append("Toyota")
print(cars)
cars.append("Benz")
print(cars)
cars.append("BMW")
print(cars)

# insert()插入元素(可以直接指定索引的位置安插進去)
cars.insert(1, "Nissan")
cars.insert(2, "BMW")
print(cars)

# pop()刪除串列元素
popped_car = cars.pop()  # 刪除末端值
print("刪除末端值", popped_car, ",刪除後內容", cars)
popped_car = cars.pop(1)  # 刪除索引1的值
print("刪除索引1的值", popped_car, ",刪除後內容", cars)

# remove()刪除指定的元素
expensive = "Benz"
cars.remove(expensive)
print("移除Benz", cars)









