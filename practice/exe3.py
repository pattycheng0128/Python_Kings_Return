try:
    principal = int(input("請輸入投資的金額:"))
    rate = int(input("請輸入年利率(%):"))
    calRate = rate / 100
    year = int(input("請輸入要儲存幾年:"))

    amount = principal * (1+calRate) ** year
    print("%d年後可拿回%d元" % (year, amount))
except Exception:
    print("您輸入錯誤的內容，請輸入整數")