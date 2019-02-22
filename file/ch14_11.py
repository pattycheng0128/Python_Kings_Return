import os

totalsizes = 0
file_path = "D:\\Python課程\\Python王者歸來\\file"
# getsize()獲得特定的檔案大小
file_size = os.path.getsize("ch14_1.py")
print(file_size)

# listdir()獲得特定工作目錄的內容
list_dir = os.listdir(file_path)
print(list_dir)

# 列出特定工作目錄所有檔案的大小
for file in os.listdir(file_path):
    print(file)
    totalsizes += os.path.getsize(os.path.join(file_path, file))

print("全部檔案的大小是:", totalsizes)