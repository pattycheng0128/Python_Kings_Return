# 封裝成私有有兩個底線__
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
        self.__balance = self.__balance - self.result
        print(self.__name.title(), "目前餘額", self.__balance)

    # 美金兌換台幣方法
    def usa_to_taiwan(self, usa_d):
        self.result = self.__cal_rate(usa_d)
        return self.result

    # 計算換匯的私有方法
    def __cal_rate(self, usa_d):
        return int(usa_d * self.__rate * (1 - self.__service_change))


# 呼叫函式
hungbank = Banks('hung')
hungbank.saving_money(5000) #存款5000
hungbank.withdraw_money(3000) #提款3000
hungbank.saving_money(1500) #存款1500
hungbank.usa_to_taiwan(100) #兌換100美元
print("美元兌換台幣金額:", hungbank.usa_to_taiwan(100), "元")
hungbank.get_balance()

