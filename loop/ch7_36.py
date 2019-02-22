buyers = [["James", 1030], ["Penny", 800],
          ["Lily", 2050], ["James", 600]]

gold = []
vip = []
while buyers:
    index_buyer = buyers.pop()
    if index_buyer[1] > 1000:
        vip.append(index_buyer)
    else:
        gold.append(index_buyer)
print("VIP客戶:", vip)
print("一般客戶:", gold)