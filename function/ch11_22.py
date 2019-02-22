def kitchen(unserved, served):
    """將未服務的餐點轉為已經服務"""
    print("===處理客戶所點的餐點===")
    while unserved:
        current_meal = unserved.pop()
        # 模擬出餐點過程
        print("菜單:", current_meal)
        # 將已出餐點轉為服務
        served.append(current_meal)

def show_order_meal(unserved):
    """顯示尚未服務餐點"""
    print("===以下是所點的餐點===")
    if not unserved:
        print("沒有餐點")
    for unserved_meal in unserved:
        print(unserved_meal)

def show_served_meal(served):
    """顯示已服務餐點"""
    print("===以下是已經服務的餐點===")
    if not served:
        print("沒有餐點")
    for served_meal in served:
        print(served_meal)

order_list = ["雞塊","薯條","漢堡"] #所點餐點
served_list = [] #已服務餐點

# 列出餐廳處理前的餐點
show_order_meal(order_list)
show_served_meal(served_list)

# 餐廳服務過程
kitchen(order_list[:], served_list) # 加入傳遞副本串列，這樣之前點餐的內容才不會是空串列
print("===餐廳處理結束===")

# 列出餐廳已處理後的餐點
show_order_meal(order_list)
show_served_meal(served_list)


