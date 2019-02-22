import random

min, max = 1, 10
# 隨機產生答案
ans = random.randint(min, max)
while True:
    try:
        youNum = int(input("請輸入1~10數字:"))
        if youNum == ans:
            print("您猜對了")
            break
        elif youNum < ans:
            print("數字太小了")
        else:
            print("數字太大了")
    except Exception as err:
        print("輸入的內容有誤，必須為數字",err)