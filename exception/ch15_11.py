def division(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("除數為0發生")
    except TypeError:
        print("使用字元做除法運算異常")

print(division(5, 2.5))
print(division(5, 0))
print(division(6, 2))
print(division("a", "b"))