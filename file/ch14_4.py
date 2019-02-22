import os

# 檢查路徑方式
# 1.檔案是否存在
print(os.path.exists("ch14.py"))
print(os.path.exists("ch14_4.py"))
print("--------------------------------")

# 2.是資料夾
dir1 = os.path.isdir("D:\\Python課程\\Python王者歸來\\file")
dir2 = os.path.isdir("D:\\Python課程\\Python王者歸來\\file\\ch14_4.py")
print("dir1 is %s,dir2 is %s" % (dir1,dir2))

print("--------------------------------")
# 3.是檔案
file1 = os.path.isfile("D:\\Python課程\\Python王者歸來\\file")
file2 = os.path.isfile("D:\\Python課程\\Python王者歸來\\file\\ch14_4.py")
print("file1 is %s,file2 is %s" % (file1,file2))