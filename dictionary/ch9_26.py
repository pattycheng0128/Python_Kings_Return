wechat_account = {"Lily": {"last_name": "黃", "first_name": "美麗",
                           "city": "Taipei"},
                  "Penny": {"last_name": "韓", "first_name": "佳人",
                            "city": "Tainan"}}

for account, account_info in wechat_account.items():
    print("使用者帳號:", account)
    name = account_info["last_name"] + account_info["first_name"]
    print("姓名:", name)
    print("居住城市:", account_info["city"])
    print("----------------------------")

