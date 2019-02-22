#封裝成私有有兩個底線__
class Banks():
    
    # 初始化方法，設定存款者的姓名和存款
    def __init__(self, uname, money):
        # name和balance是設計的屬性
        self.__name = uname  # 姓名
        self.__balance = money  # 存款
        self.__title = "Taipei"  # 存款銀行
        
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


hungbank = Banks("hung", 1000)
# 無法竄改金額原金額
hungbank.balance = 6000
hungbank.get_balance()
