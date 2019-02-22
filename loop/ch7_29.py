answer = 30
guess = 0
while guess != answer:
    guess = int(input("請輸入數字:"))
    if guess > answer:
        print("數字太大了")
    elif guess < answer:
        print("數字太小了")
    else:
        print("恭喜答對了")