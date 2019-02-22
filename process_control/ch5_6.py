print("===計算票價優惠===")
age = input("請輸入年齡:")
age = int(age)
ticket = 100
if age >= 80 or age <= 6:
    print("您的票價2折:", ticket*0.2)
elif age >= 60 or age <= 12:
    print("您的票價是5折:", ticket*0.5)
else:
    print("原價", ticket)
