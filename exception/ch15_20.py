class Banks():

    title = "Taipei Bank"
    def __init__(self, uname, money):
        self.name = uname
        self.balace = money
    #設計存款
    def saving_money(self, money):
        assert money > 0, "存款必須大於0"
        self.balace += money
        print("存款:", money, "完成")

    #設計提款
    def withdraw_money(self, money):
        assert money > 0, "提款金額必須大於0"
        assert money <= self.balace, "存款金額不足"
        self.balace -= money
        print("提款:", money, "完成")

    def get_balance(self):
        print(self.name.title(), "目前餘額:", self.balace)

hung = Banks('hung', 1000)
# hung.saving_money(0)  # 印出錯誤訊息
# hung.withdraw_money(1100)  # 印出錯誤訊息
hung.withdraw_money(300)
hung.saving_money(100)
hung.get_balance()

