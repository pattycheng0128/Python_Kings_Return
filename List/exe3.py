print("宴客名單")
try:
    banquet = ["Penny", "Lily", "John", "Tom"]
    ch = int(input("請選擇要更動的宴客內容(1.要新增人數 2.要刪除人數 3.無更動):\n"))
    if ch == 1:
        name = input("請輸入要新增的宴客姓名")
        banquet.append(name)
        print(banquet)
    elif ch == 2:
        name = input("請輸入要刪除的宴客姓名")
        banquet.remove(name)
        print(banquet)
    else:
        print("尚未變動人數")
except Exception:
    print("您輸入錯誤")

