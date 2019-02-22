fn = "test.txt"
# 用with的好處是不必在程式中關閉檔案
with open(fn) as file_Obj:
    data = file_Obj.read()
    print(data)
    print("--------------------------------------------------------")
    # 刪除末端的空白行
    print(data.rstrip())
