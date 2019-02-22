class Banks():
    title = "Taipei"

    # 初始化的方法
    def __init__(self, uname, money):
        self.name = uname  # 設定存款者的名字
        self.balance = money  # 儲存的金額
        
    def get_balance(self):
        return self.balance

    
hungbank = Banks("hung", 100)  # 定義物件hungbank
print(hungbank.name.title(), "存款餘額是:", hungbank.get_balance())
    
