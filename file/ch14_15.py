# 檔案名稱
fn = "test.txt"
# 開啟檔案，預設是read
file_Obj = open(fn)
# 讀取檔案
data = file_Obj.read()
# 關閉檔案
file_Obj.close()
print(data)