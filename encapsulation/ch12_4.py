class Banks():
    
    # 初始化方法，設定存款者的姓名和存款
    def __init__(self, uname, money):
        # name和balance是設計的屬性
        self.name = uname  # 姓名
        self.balance = money  # 存款
        self.title="Taipei" # 存款銀行
        
    # 設計存款方法
    def saving_money(self, money):
        self.balance = self.balance + money
        print("存款金額:", money)
    
    # 設計提款方法
    def withdraw_money(self, money):
        self.balance = self.balance - money
        print("提款金額:", money)
    
    # 獲得存款餘額
    def get_balance(self):
        print(self.name.title(), "目前餘額", self.balance)


hungbank = Banks("hung", 1000)
# 原金額
hungbank.get_balance()
# 存錢
hungbank.saving_money(1000)
# 提錢
hungbank.withdraw_money(200)
# 存款餘額
hungbank.get_balance()
# 竄改金額原金額
hungbank.balance = 5000
hungbank.get_balance()

"""Hung 目前餘額 1000
存款金額: 1000
提款金額: 200
Hung 目前餘額 1800
Hung 目前餘額 5000"""
