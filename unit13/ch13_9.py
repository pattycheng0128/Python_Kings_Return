from unit13 import banks

# 呼叫記得要先建立物件
patty = banks.Banks("patty")  # 建立物件
patty.get_balance()
patty.save_money(1000)
patty.withdraw_money(100)
patty.get_balance()
print("-----------------------------------")
penny = banks.Shilin_Banks("patty")  # 建立士林分行物件
print(penny.bank_title())


