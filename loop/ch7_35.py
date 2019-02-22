fruits = ["apple", "orange", "apple", "banana", "apple"]
fruit = "apple"
print("原內容", fruits)
while fruit in fruits:
    fruits.remove(fruit)
print("移除apple後的內容:", fruits)