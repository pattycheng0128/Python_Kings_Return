players = ["AA", "BB", "CC", "DD", "EE", "FF", "GG"]
n = int(input("請輸入人數:"))
if n > len(players) : n = len(players)
index = 0

while index < len(players):
    if index == n:
        break
    print(players[index], end=" ")
    index += 1