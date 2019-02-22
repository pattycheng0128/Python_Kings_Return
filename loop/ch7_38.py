drinks = ["coffee", "tea", "wine"]
for drink in enumerate(drinks):
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("***************")
# 解析enumerate
for drink in enumerate(drinks, 10):
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)