def divison(x, y):
    try:
        ans = x / y
    except ZeroDivisionError:
        print("除數不可為0")
    else:
        return ans

print(divison(5, 4))
print(divison(5, 0))
print(divison(5, 0))
