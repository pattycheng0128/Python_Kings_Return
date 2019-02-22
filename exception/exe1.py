def division(x, y):
    try:
        return x/y
    except(ZeroDivisionError, TypeError) as e:
        print(e)


print(division(6, 2))
print(division(6, 0))
print(division("a", "b"))