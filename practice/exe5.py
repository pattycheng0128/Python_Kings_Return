year = int(input("請輸入年份:"))

if year % 4 == 0:
    if (year % 100 != 0) or (year % 400 == 0):
        print("是潤年")
    else:
        print("不是潤年")
else:
    print("不是潤年")