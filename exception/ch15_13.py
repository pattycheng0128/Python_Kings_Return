def division(x, y):
    try:
        return x/y
    except (ZeroDivisionError, TypeError) as e:
        print(e)

print(division(5, 2.5))
print(division(5, 0))
print(division(6, 2))
print(division("a", "b"))