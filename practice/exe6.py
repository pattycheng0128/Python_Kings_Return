try:
    hourly_salary = int(input("請輸入時薪:"))  # 時薪
    monthly_fee = int(input("請輸入月花費:"))  # 月支出

    annual_salary = hourly_salary * 8 * 300  # 年薪
    annual_fee = monthly_fee * 12  # 年支出
    annual_savings = annual_salary - annual_fee  # 年儲蓄
    print(annual_savings)
except Exception as err:
    print("輸入必須為數字", err)


