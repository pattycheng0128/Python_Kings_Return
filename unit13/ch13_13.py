from unit13 import shilin_bank
from unit13 import banks

# 建立士林分行的物件
patty = shilin_bank.Shilin_Banks("patty")
print(patty.bank_title())

# 建立Banks物件
penny = banks.Banks("penny")
penny.get_balance()
penny.save_money(1000)
penny.withdraw_money(100)
penny.get_balance()
