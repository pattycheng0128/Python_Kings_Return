fruits = ["apple", "banana", "orange", "grape"]
fruit = input("請輸入水果:")
if fruit in fruits:
    print("這個水果以在清單內囉")
else:
    fruits.append(fruit)
    print("已加入清單:", fruits)