import json

fn = "login24_10.json"

# 第一次會先讀取資料
try:
    with open(fn) as fnObj:
        login = json.load(fnObj)
except Exception:
    login = input("請輸入帳號:")
    with open(fn, "w") as fnObj:
        json.dump(login, fnObj)
        print("系統已經紀錄你的帳號")
else:
    print("%s歡迎回來!" % login)