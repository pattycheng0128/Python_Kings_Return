import random

min, max = 1, 50
winPercent = int(input("請輸入莊家贏的比例(0-50)之間:"))
if winPercent < 0 or winPercent > 50:
    print("值輸入錯誤")
    winPercent = int(input("請輸入莊家贏的比例(0-50)之間:"))

while True:
    customerNum = input("猜大小遊戲:L或l表示大，S或s表示小，Q或q則離開程式:\n")
    if customerNum == "Q" or customerNum == "q":
        break
    # 產生是否讓玩家答對的隨機數字
    num = random.randint(min, max)
    if num > winPercent:
        print("恭喜答對了", num)
    else:
        print("答錯了!再試一次", num)