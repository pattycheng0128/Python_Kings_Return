import random
import time

min, max = 1, 10
ans = random.randint(min, max)  # 隨機產生答案
# 起始秒數
starttime = int(time.time())
while True:
    yourNum = int(input("請輸入1~10數字:"))
    if yourNum == ans:
        print("您答對了")
        endtime = int(time.time())
        print("所花時間:", endtime-starttime, "秒")
        break
    elif yourNum < ans:
        print("數字太小囉!")
    else:
        print("數字太大囉!")
