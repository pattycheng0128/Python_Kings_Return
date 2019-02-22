import random


class Lottery():
    def __init__(self):
        self.__company = {1: "Lily", 2: "Penny", 3: "John", 4: "Ken", 5: "Ben",
                         6: "Jim", 7: "Rita", 8: "Rose", 9: "Sally", 10: "Sharon"}

    def winning(self):
        try:
            num, name = random.choice(list(self.__company.items()))
            print("恭喜%s號%s中獎了!!" % (num, name))
            del self.__company[num]
            # print(len(self.__company))
        except Exception:
            print("清單已無內容")


test = Lottery()
test.winning()
test.winning()
test.winning()
test.winning()