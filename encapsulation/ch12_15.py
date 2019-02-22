class Grandfather():

    def __init__(self):
        self.grandfathermoney = 10000

    def get_info1(self):
        print("Grandfather's information")

        
class father(Grandfather):

    def __init__(self):
        self.fathermoney = 5000
        super().__init__()
        

    def get_info2(self):
        print("Father's information")

        
class Ivan(father):

    def __init__(self):
        self.Ivymoney = 1000
        super().__init__()

    def get_info3(self):
        print("Ivy's information")
        
    def get_money(self):
        print("\nIvy資產:", self.Ivymoney,
              "\nFather資產:", self.fathermoney,
              "\nGrandfather資產:", self.grandfathermoney)


ivan = Ivan()  # 建立物件
ivan.get_info1()
ivan.get_info2()
ivan.get_info3()
ivan.get_money()








