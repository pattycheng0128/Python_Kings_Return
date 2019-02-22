import glob

print("方法1--------------------,列出目錄下所有的檔案")
for file in glob.glob("D:\\Python課程\\Python王者歸來\\file\\*.*"):
    print(file)

print("方法2--------------------,列出目錄下特定的檔案")
for file in glob.glob("ch14_1*.py"):
    print(file)


print("方法3--------------------,列出目錄下特定的檔案")
for file in glob.glob("ch14_1*.*"):
    print(file)
