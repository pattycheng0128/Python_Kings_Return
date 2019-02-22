# 設定欲開啟的檔案
fn = "test.txt"
# 傳回檔案物件file_Obj
with open(fn) as file_Obj:
    # 每次讀一行
    obj_list = file_Obj.readlines()
# 設定空字串
str_Obj = ""
# 將各行的字串存入
for line in obj_list:
    str_Obj += line.rstrip()

findstr = input("請輸入要搜尋的字串:")
index = str_Obj.find(findstr)
if index >= 0:
    print("搜尋%s字串在%s檔案中" % (findstr,fn))
    print("在索引%s位置出現" % index)
else:
    print("搜尋%s字串不存在%s檔案中" % (findstr, fn))
