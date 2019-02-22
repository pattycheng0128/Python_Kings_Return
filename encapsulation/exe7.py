class Father():
    def __init__(self):
        self.fathermoney = 10000


class Ira(Father):
    def __init__(self):
        self.iramoney = 1000
        super().__init__()

    def get_money(self):
        print("Ira資產", self.iramoney,
              "\n父親資產", self.fathermoney,
              "\nIva", Ivy().ivymoney)


class Ivy(Father):
    def __init__(self):
        self.ivymoney = 2000
        super().__init__()

    def get_money(self):
        print("Ivy資產", self.ivymoney,
              "\n父親資產", self.fathermoney,
              "\nIra", Ira().iramoney)


# 呼叫
child2 = Ira()
child2.get_money()
