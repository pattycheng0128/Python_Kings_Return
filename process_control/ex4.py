try:
    amount = int(input("請輸入今日消費金額:"))
    age = int(input("請輸入您的年齡:"))

    if amount >= 100000:
        print("打9折:", amount*0.9)
    elif amount >= 80000 or age == 50:
        print("打95折:", amount*0.95)
    elif amount >= 50000:
        print("打98折:", amount * 0.98)
    else:
        print("金額未滿50000，沒有折扣。\n今日消費金額:", amount)
except ValueError:
    print("您輸入錯誤內容")