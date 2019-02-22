armys = []  # 建立空陣列
for soldier_number in range(50):
    soldier = {"tag": "red", "score": 3, "speed": "slow"}
    armys.append(soldier)
print("列印前3名的小兵")
for soldier in armys[:3]:
    print(soldier)
    print("------------------------------------")
# 更改編號36~38的小兵
for soldier in armys[35:38]:
    if soldier["tag"] == "red":
        soldier["tag"] = "blue"
        soldier["score"] = 5
        soldier["speed"] = "medium"

# 列印編號35~40的小兵
for soldier in armys[34:40]:
    print(soldier)