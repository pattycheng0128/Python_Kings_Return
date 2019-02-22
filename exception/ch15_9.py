def divison(x, y):
    try:
        return x/y
    except Exception:
        print("通用錯誤發生")

print(divison(6, 2))
print(divison(6, 0))
print(divison(2, 2))
