Python_read = ("Any", "Anna", "Penny", "Jim", "Bob")
# 用for迴圈列印組員
for read in Python_read:
    print(read)
# 重新設定組員人數，增加至8人
print("*********************************")
Python_read = ("Any", "Anna", "Penny", "Jim", "Bob", "Poc", "Tom", "Carry")
for read in Python_read:
    print(read)
# 嘗試修改，然後得到錯誤訊息
print("*********************************")
Python_read[0] = "Jenny"
print(Python_read)
