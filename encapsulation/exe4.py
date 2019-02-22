class Banks():

    # 初始化方法，將一些預設的屬性放在裡面
    def __init__(self, uname):  # uname是在呼叫函式須設定的參數
        self.__name = uname  # 姓名
        self.__balance = 0  # 存款
        self.__title = "Taipei"  # 存款銀行
        self.__rate = 30  # 預設美金和台幣的換匯比例
        self.__service_change = 0.01  # 手續費

    # 設計存款方法
    def saving_money(self, money):
        self.__balance += money
        print("存款金額:", money)

    # 設計提款方法
    def withdraw_money(self, money):
        self.__balance -= money
        print("提款金額:", money)

    # 獲得存款餘額
    def get_balance(self):
        print(self.__name.title(), "目前餘額", self.__balance)

    # 美金兌換台幣方法
    def usa_to_taiwan(self, usa_d):
        self.result = self.__cal_rate(usa_d)
        return self.result

    # 計算換匯的私有方法
    def __cal_rate(self, usa_d):
        return int(usa_d * self.__rate * (1 - self.__service_change))


# 士林分行
class ShilinBanks(Banks):
    def __init__(self, uname):
        self.title = "Shilin Branch"

    def bank_title(self):
        return self.title


# 北投分行
class Beitou(Banks):
    def __init__(self, uname):
        self.title = "Beitou Branch"

    def bank_title(self):
        return self.title


# 呼叫
bank = ShilinBanks("Patty")
print("Hello Patty", bank.bank_title())

bank2 = Beitou("Patty")
print("Hello Patty", bank2.bank_title())
