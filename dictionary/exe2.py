fruits = {"apple": 30, "orange": 10, "banana": 15}

while True:
    key = input("請輸入要查詢的內容(key):(q離開)")
    if key == "q":
        break
    else:
        value = input("請輸入要查詢的內容(value):")
        if key in fruits:
           print("在字典內", key)
        else:
            fruits[key] = value
            print("加入字典", fruits)