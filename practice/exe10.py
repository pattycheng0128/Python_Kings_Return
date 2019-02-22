class Bank():

    def __init__(self, uname):
        self.__name = uname
        self.__balance = 0

    def save_money(self, money):
        self.__balance += money
        print("存款", money, "完成")

    def withdraw_money(self, money):
        self.__balance -= money
        print("提款", money, "完成")

    def get_balance(self):
        print(self.__name, "目前餘額:", self.__balance)


test = Bank("Patty")
test.get_balance()
test.save_money(1000)
test.withdraw_money(100)
test.get_balance()