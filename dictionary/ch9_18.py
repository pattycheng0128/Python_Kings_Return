players = {"Sherry": "Gold",
           "Kevin": "Gold",
           "James": "Gold",
           "Paul": "Gold"}
for name in players.keys():
    print("姓名:", name)
print("-------------------")
# .keys可以省略
for name in players:
    print("姓名:", name)
print("-------------------")
for team in players.values():
    print("隊友:", team)