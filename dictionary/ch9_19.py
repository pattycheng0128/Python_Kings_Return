players = {"Sherry": "Gold",
           "Kevin": "Gold",
           "James": "Gold",
           "Paul": "Gold"}

for name in sorted(players.keys()):
    print(name)
    print(name, players[name])
    print("------------------")