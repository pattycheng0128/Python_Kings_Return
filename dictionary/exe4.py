travel_country = {"Taiwan": {"location1": "Tainan",
                             "location2": "Taipei",
                             "location3": "Taoyuan",
                             "location4": "Taipei",
                             "location5": "Taipei"}}

for travel, location in travel_country.items():
    print("國家:", travel)
    print("城市:", location["location1"])
    print("城市:", location["location2"])
    print("城市:", location["location3"])
    print("城市:", location["location4"])
    print("城市:", location["location5"])