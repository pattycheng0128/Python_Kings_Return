fruits = ["李子", "香蕉", "蘋果", "西瓜", "桃子"]
i = 0
# 使用enumerate
for fruit in enumerate(fruits, 1):
    print(fruit)

# 使用迴圈
for fruit in fruits:
    i += 1
    print(i, ":", fruit)