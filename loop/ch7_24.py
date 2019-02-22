players = [["James", 202], ["Curry", 180],
           ["David", 100], ["Lily", 250]]

for player in players:
    if player[1] < 200:
        continue
    print(player)