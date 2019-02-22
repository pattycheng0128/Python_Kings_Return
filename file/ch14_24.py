# 設定欲開啟的檔案
fn = "test.txt"
# 用預設read開啟檔案，傳回檔案物件file_obj
with open(fn) as file_Obj:
    obj_list = file_Obj.readlines()  # 每次讀一行

# 先設為空字串
str_Obj = ""
# 將各行的空字串存入
for line in obj_list:
    str_Obj += line.rstrip()

findstr = input("請輸入要搜尋的字串=")
if findstr in str_Obj:
    print("搜尋%s字串存在%s檔案中" %(findstr,fn))
else:
    print("搜尋%s字串不存在%s檔案中" % (findstr, fn))
