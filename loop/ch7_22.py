players = ["AA", "BB", "CC", "DD", "EE", "FF", "GG"]
n = int(input("請輸入人數:"))
if n > len(players) : n = len(players)
index = 0
for player in players:
    if index == n:
        break
    print(player, end=" ")
    index += 1