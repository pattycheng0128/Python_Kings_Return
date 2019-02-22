try:
    num = int(input("請輸入負值:"))
    print("計算絕對值", abs(num))
except Exception as err:
    print("您輸入錯誤", err)