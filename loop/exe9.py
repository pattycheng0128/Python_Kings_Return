buyers = [["James", 2000], ["Penny", 15000],
          ["David", 700], ["Lily", 400], ["John", 500], ["cary", 200]]

goldbuyers = []
vipbuyers = []
infinitebuyers = []
while buyers:
    index_buyer = buyers.pop()
    if index_buyer[1] >= 10000:
        infinitebuyers.append(index_buyer)
    elif index_buyer[1] >= 1000:
        vipbuyers.append(index_buyer)
    else:
        goldbuyers.append(index_buyer)
print("infinite買家:", infinitebuyers)
print("vip買家:", vipbuyers)
print("gold買家:", goldbuyers)