try:
    num = input("請輸入數字:")
    num = int(num)

    if num < 0:
        print(abs(num))
    else:
        print(-num)
except ValueError:
    print("您輸入錯誤，請輸入數字")