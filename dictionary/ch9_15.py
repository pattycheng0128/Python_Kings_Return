fruits = {"apple": 30, "orange": 10, "banana": 15}
key = input("請輸入要查詢的內容(key):")
value = input("請輸入要查詢的內容(value):")
if key in fruits:
    print("已經在字典", key)
else:
    fruits[key] = value  # 如果輸入的內容部在清單內，自動將內容加入
    print("新增到字典內", fruits)