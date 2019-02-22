def divison(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("除數不可為0")

print(divison(5, 4))
print(divison("a", "b"))
print(divison(5, 0))
