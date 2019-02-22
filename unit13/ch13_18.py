import random

porker = ["1", "2", "3", "4", "5", "6", "7", "8",
          "9", "10", "J", "Q", "K"]
print("洗牌前:", porker)
random.shuffle(porker)
print("洗牌後:", porker)