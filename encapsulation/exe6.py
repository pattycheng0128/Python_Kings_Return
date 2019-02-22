class Grandfather():

    def __init__(self):
        self.grandfathermoney = 10000

    def get_info1(self):
        print("Grandfather's information")
class Grandmother():

    def __init__(self):
        self.grandmothermoney = 20000

    def get_info2(self):
        print("Grandmother's information")
class Father (Grandfather,Grandmother):

    def __init__(self):
        self.fathermoney = 5000
        super().__init__()
        super(Grandfather, self).__init__()
        super(Grandmother, self).__init__()

    def get_info3(self):
        print("Father's information")


class Ivan(Father):

    def __init__(self):
        self.Ivymoney = 1000
        super().__init__()

    def get_info4(self):
        print("Ivy's information")

    def get_money(self):
        print("\nIvy資產:", self.Ivymoney,
              "\nFather資產:", self.fathermoney,
              "\nGrandfather資產:", self.grandfathermoney,
              "\nGrandmother資產:", self.grandmothermoney)

#呼叫
ivan = Ivan()
ivan.get_money()








