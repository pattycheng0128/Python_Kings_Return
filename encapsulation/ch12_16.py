class Father():
    def __init__(self):
        self.fathermoney = 10000

        
class Ira(Father):
    def __init__(self):
        self.iramoney = 1000
        super().__init__()

        
class Ivy(Father):
    def __init__(self):
        self.ivymoney = 2000
        super().__init__()

    def get_money(self):
        print("Lily資產", self.ivymoney,
              "\n父親資產", self.fathermoney,
              "\nIra", Ira().iramoney)


# 呼叫
child = Ivy()
child.get_money()
child2=Ira()
child2.fathermoney
