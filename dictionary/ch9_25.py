sports = {"Curry": ["籃球", "美式足球"],
          "Durant": ["棒球"],
          "James": ["美式足球", "棒球", "籃球"]}

for name, favorite_sport in sports.items():
    print("%s喜歡的運動是:" % name)

    for sport in favorite_sport:
        print(sport)