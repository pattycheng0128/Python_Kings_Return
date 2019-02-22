year = int(input("請輸入年份是否為潤年:"))
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("為潤年")
    else:
        print("不為潤年")
else:
    print("不為潤年")