drinks = {"coffee", "tea", "juice"}
enumerate_drinks = enumerate(drinks)
print(enumerate_drinks)  # 傳回是物件所在的記憶體位置
print(type(enumerate_drinks))
# 轉成串列輸出
print(list(enumerate_drinks))
print("-----------------------------")
# 迴圈輸出
for count, item in enumerate(drinks):
    print(count, item)
print("-----------------------------")
for count, item in enumerate(drinks, 10):
    print(count, item)