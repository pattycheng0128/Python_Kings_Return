try:
    month_hour = int(input("請輸入這個月的工作時數:"))
    hour_salary = 150
    if month_hour > 150:
        print("您的月薪是1.6倍:", (month_hour * hour_salary) * 1.6)
    elif (month_hour > 120) and (month_hour <= 150):
        print("您的月薪是1.2倍:", (month_hour * hour_salary) * 1.2)
    elif month_hour == 120:
        print("您的月薪是:", month_hour * hour_salary)
    elif month_hour < 120:
        print("您的月薪是0.8倍:", (month_hour * hour_salary)*0.8)
    else:
        print("您輸入錯誤")
except ValueError:
    print("您輸入錯誤的格式")