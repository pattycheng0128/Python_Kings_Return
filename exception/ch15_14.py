def division(x, y):
    try:
        return x/y
    except:
        print("異常發生")

print(division(5, 2.5))
print(division(5, 0))
print(division(6, 2))
print(division("a", "b"))