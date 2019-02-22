def division(x, y):
    try:
        return x/y
    except:
        print("異常發生")
    finally:
        print("階段任務完成")

print(division(5, 2), "\n")
print(division(5, 0), "\n")
print(division("a", "b"), "\n")