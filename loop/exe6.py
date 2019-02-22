answer = 30
guess = 0
count = 0
while guess != answer:
    guess = int(input("請輸入1~100間的數字:"))
    count += 1
    if guess > answer:
        print("數字太大了")
    elif guess < answer:
        print("數字太小了")
    else:
        print("你猜對了!", "共猜了", count, "次")