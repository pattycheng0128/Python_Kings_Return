survey_dict = {}
market_survey = True

while market_survey:
    name = input("請輸入姓名:")
    travel_location = input("請輸入旅遊地點:")

    # 將內容存入字典
    survey_dict[name] = travel_location

    # 是否離開市場調查
    repeat = input("是否要參加市場調查:(y/n)")
    if repeat != "y":
        market_survey = False

print("以下是市場調查的結果")
for user, location in survey_dict.items():
    print(user, "夢幻旅遊景點", location)