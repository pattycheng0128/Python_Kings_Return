"""**players可以接受任意數量的關鍵字參數"""
def buld_dict(name, age, **players):
    info = {}
    info["Name"] = name
    info["Age"] = age
    for key, values in players.items():
        info[key] = values
    return info # 回傳所建的字典

player_dict = buld_dict("James", "32", City= "Taipei", State = "city")
print(player_dict)
