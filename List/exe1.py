travel = ["Taiwan", "France", "America", "China",
          "Singapore", "Finland", "Malaysia", "Switzerland",
          "Japan", "Korea"]
print("My favorite country:", travel)
# 反向排序
travel.reverse()
print(travel)
# sort字母A~Z
travel.sort()
print(travel)
# sort (reverse=true)字母Z~A
travel.sort(reverse=True)
print(travel)
# 在index = 0 新增內容
travel.insert(0, "Antarctic")
print(travel)
# 在最後index加入內容
travel.append("Arctic Sea")
print(travel)
# 在中間位置新增內容
print("串列長度", len(travel))  # 計算目前內容長度
travel.insert(6, "Chicago")
print(travel)
print("串列長度", len(travel))
# 刪除第3和第9筆資料
del3 = travel[2]
del9 = travel[8]
print("刪除第3筆資料", del3)
print("刪除第9筆資料", del9)



